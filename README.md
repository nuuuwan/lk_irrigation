# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--19_05:18:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **155,784 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 05:18:13 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.017 |  |
| 2026-05-19 05:14:11 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | -0.135 |  |
| 2026-05-19 05:13:04 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.021 |  |
| 2026-05-19 05:12:32 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.084 |  |
| 2026-05-19 05:12:27 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-19 05:08:47 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-19 05:07:59 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | -0.026 |  |
| 2026-05-19 05:07:55 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 05:07:30 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -2.118 |  |
| 2026-05-19 05:07:13 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | -2.118 |  |
| 2026-05-19 05:06:13 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.009 |  |
| 2026-05-19 05:06:03 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.008 |  |
| 2026-05-19 05:05:44 | Giriulla (Maha Oya) | 1.69 | 🟢 Normal | -0.020 |  |
| 2026-05-19 05:05:31 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-19 05:04:57 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.046 |  |
| 2026-05-19 05:04:34 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-19 05:04:32 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.030 |  |
| 2026-05-19 05:04:13 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.003 |  |
| 2026-05-19 05:04:03 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-19 05:03:54 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-05-19 05:02:53 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 05:02:39 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-05-19 05:02:33 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.019 |  |
| 2026-05-19 05:02:21 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-05-19 05:02:17 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-19 05:02:16 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-19 05:01:47 | Moragaswewa (Deduru Oya) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-05-19 05:01:39 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | -0.005 |  |
| 2026-05-19 05:01:38 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.030 |  |
| 2026-05-19 05:01:37 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-19 05:01:36 | Rathnapura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.020 |  |
| 2026-05-19 05:01:29 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.285 |  |
| 2026-05-19 05:00:29 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 05:02:39 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-05-19 05:05:31 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-19 05:08:47 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-19 05:02:16 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-18 18:01:40 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-19 05:00:29 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-05-19 05:07:55 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 05:04:03 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-19 05:12:27 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-19 05:02:53 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 05:02:21 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-05-19 05:04:34 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-19 04:01:01 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-19 05:01:37 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-19 05:02:17 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-19 05:04:13 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.003 |  |
| 2026-05-19 05:01:39 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | -0.005 |  |
| 2026-05-19 05:06:03 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.008 |  |
| 2026-05-19 05:06:13 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.009 |  |
| 2026-05-19 05:03:54 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-05-19 05:18:13 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.017 |  |
| 2026-05-19 04:10:02 | Magura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.019 |  |
| 2026-05-19 05:02:33 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.019 |  |
| 2026-05-19 05:05:44 | Giriulla (Maha Oya) | 1.69 | 🟢 Normal | -0.020 |  |
| 2026-05-19 05:01:36 | Rathnapura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.020 |  |
| 2026-05-19 05:01:47 | Moragaswewa (Deduru Oya) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-05-19 05:13:04 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.021 |  |
| 2026-05-19 05:07:59 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | -0.026 |  |
| 2026-05-19 04:08:23 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | -0.028 |  |
| 2026-05-19 05:04:32 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.030 |  |
| 2026-05-19 05:01:38 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.030 |  |
| 2026-05-18 18:01:53 | Galgamuwa (Mee Oya) | 1.67 | 🟢 Normal | -0.033 |  |
| 2026-05-19 05:04:57 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.046 |  |
| 2026-05-19 03:25:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.44 | 🟢 Normal | -0.068 |  |
| 2026-05-18 18:01:24 | Thanthirimale (Malwathu Oya) | 2.75 | 🟢 Normal | -0.082 |  |
| 2026-05-19 05:12:32 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.084 |  |
| 2026-05-19 05:14:11 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | -0.135 |  |
| 2026-05-19 05:01:29 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.285 |  |
| 2026-05-19 05:07:30 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -2.118 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)