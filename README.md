# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--18_05:16:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **182,407 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 05:16:58 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:12:02 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:08:35 | Rathnapura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.107 |  |
| 2026-06-18 05:07:57 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | -0.019 |  |
| 2026-06-18 05:07:23 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 05:06:53 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:06:30 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:06:07 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:05:58 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:05:57 | Glencourse (Kelani Ganga) | 10.93 | 🟢 Normal | -0.107 |  |
| 2026-06-18 05:05:39 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.033 |  |
| 2026-06-18 05:05:14 | Hanwella (Kelani Ganga) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:04:51 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:03:46 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | -0.040 |  |
| 2026-06-18 05:03:38 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:03:20 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.040 |  |
| 2026-06-18 05:02:21 | Dunamale (Aththanagalu Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:02:20 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.123 |  |
| 2026-06-18 05:02:14 | Pitabeddara (Nilwala Ganga) | 1.53 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-18 05:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-06-18 05:01:37 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:01:34 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:01:31 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:01:16 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-06-18 05:01:14 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 05:01:04 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:00:59 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:00:52 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:00:50 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-18 04:52:56 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-06-18 04:28:53 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 04:04:44 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-06-18 05:02:14 | Pitabeddara (Nilwala Ganga) | 1.53 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-18 04:08:50 | Panadugama (Nilwala Ganga) | 3.78 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-18 04:25:45 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-18 05:01:14 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 05:07:23 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 04:04:04 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 04:02:37 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-18 04:06:32 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:02:56 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:01:34 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:00:52 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:00:59 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:16:58 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:03:38 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:01:37 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:05:14 | Hanwella (Kelani Ganga) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:05:58 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:06:30 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:01:31 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:01:04 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:12:02 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:02:21 | Dunamale (Aththanagalu Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:04:51 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:06:07 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:06:53 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:01:16 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-06-17 18:05:17 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-06-17 18:01:25 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-06-18 05:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-06-18 05:07:57 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | -0.019 |  |
| 2026-06-18 04:04:16 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.021 |  |
| 2026-06-18 04:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.28 | 🟢 Normal | -0.025 |  |
| 2026-06-18 05:05:39 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.033 |  |
| 2026-06-18 05:03:20 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.040 |  |
| 2026-06-18 05:03:46 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | -0.040 |  |
| 2026-06-18 05:08:35 | Rathnapura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.107 |  |
| 2026-06-18 05:05:57 | Glencourse (Kelani Ganga) | 10.93 | 🟢 Normal | -0.107 |  |
| 2026-06-18 05:02:20 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.123 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)