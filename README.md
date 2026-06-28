# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--28_16:19:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **191,794 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 16:19:09 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-28 16:18:41 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-28 16:17:49 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.009 |  |
| 2026-06-28 16:15:46 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:10:53 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:08:07 | Rathnapura (Kalu Ganga) | 1.16 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-06-28 16:07:31 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | -0.019 |  |
| 2026-06-28 16:07:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:06:37 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:06:37 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 16:06:37 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.086 |  |
| 2026-06-28 16:06:01 | Ellagawa (Kalu Ganga) | 5.02 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:05:54 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-28 16:05:22 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-06-28 16:05:16 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | -0.019 |  |
| 2026-06-28 16:04:58 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:04:57 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-28 16:04:24 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:04:21 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:04:14 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:04:04 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:03:50 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:03:34 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:03:14 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:03:12 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:03:12 | Glencourse (Kelani Ganga) | 9.78 | 🟢 Normal | -0.010 |  |
| 2026-06-28 16:02:43 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:02:34 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:02:26 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-06-28 16:02:01 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:01:44 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:01:34 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:01:26 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:01:19 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.005 |  |
| 2026-06-28 16:01:14 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:01:13 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:59:06 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 16:08:07 | Rathnapura (Kalu Ganga) | 1.16 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-06-28 16:04:57 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-28 16:05:54 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-28 16:19:09 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-28 16:18:41 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-28 16:06:37 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 16:03:50 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:03:12 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:01:13 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:01:14 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:03:14 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:02:01 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:02:43 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:15:46 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:04:14 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:04:04 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:04:24 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:06:01 | Ellagawa (Kalu Ganga) | 5.02 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:04:58 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:03:59 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:03:34 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:01:26 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:59:06 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:02:34 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:10:53 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:02:10 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:06:37 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:04:21 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:01:34 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:01:44 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:07:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-06-28 16:01:19 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.005 |  |
| 2026-06-28 16:17:49 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.009 |  |
| 2026-06-28 16:02:26 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-06-28 16:05:22 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-06-28 16:03:12 | Glencourse (Kelani Ganga) | 9.78 | 🟢 Normal | -0.010 |  |
| 2026-06-28 16:07:31 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | -0.019 |  |
| 2026-06-28 16:05:16 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | -0.019 |  |
| 2026-06-28 16:06:37 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.086 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)