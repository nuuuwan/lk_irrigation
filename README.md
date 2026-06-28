# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--28_15:09:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **191,757 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 15:09:31 | Ellagawa (Kalu Ganga) | 5.02 | 🟢 Normal | -0.009 |  |
| 2026-06-28 15:09:10 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.030 |  |
| 2026-06-28 15:08:45 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-06-28 15:08:18 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:07:45 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | -0.009 |  |
| 2026-06-28 15:07:11 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-28 15:07:03 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:06:53 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:05:49 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-06-28 15:05:39 | Glencourse (Kelani Ganga) | 9.79 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-28 15:05:01 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-28 15:04:36 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-28 15:04:31 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:04:07 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 15:03:59 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:03:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-28 15:03:42 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:03:23 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:03:18 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-06-28 15:03:07 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.031 |  |
| 2026-06-28 15:03:05 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:02:38 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-28 15:02:33 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-06-28 15:02:31 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-06-28 15:02:28 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:02:23 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:02:19 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-06-28 15:02:10 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:02:10 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:02:06 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:01:55 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:01:49 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:01:43 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-06-28 15:01:37 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:00:55 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:00:50 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 15:01:43 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-06-28 14:06:59 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-28 15:02:38 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-28 15:07:11 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-28 15:05:39 | Glencourse (Kelani Ganga) | 9.79 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-28 15:08:45 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-06-28 15:04:36 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-28 15:05:01 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-28 15:03:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-28 15:04:07 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 15:02:06 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:02:28 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:01:49 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:01:37 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:03:05 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:00:55 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:07:03 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:03:42 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:03:59 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:03:23 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:02:23 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:02:10 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:04:31 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:02:10 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:00:50 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:08:18 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:01:55 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:06:53 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-28 15:09:31 | Ellagawa (Kalu Ganga) | 5.02 | 🟢 Normal | -0.009 |  |
| 2026-06-28 15:07:45 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | -0.009 |  |
| 2026-06-28 15:02:31 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-06-28 15:05:49 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-06-28 15:02:33 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-06-28 14:01:59 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.019 |  |
| 2026-06-28 15:03:18 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-06-28 15:02:19 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-06-28 15:09:10 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.030 |  |
| 2026-06-28 15:03:07 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.031 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)