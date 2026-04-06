# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_18:27:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **117,941 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 18:27:52 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:15:11 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-06 18:10:04 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.128 |  |
| 2026-04-06 18:09:01 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:09:01 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:08:24 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:07:35 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:06:42 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-04-06 18:06:02 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:05:18 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.030 |  |
| 2026-04-06 18:04:45 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.126 |  |
| 2026-04-06 18:04:41 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | -0.013 |  |
| 2026-04-06 18:04:37 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | -0.043 |  |
| 2026-04-06 18:04:36 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:04:19 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | -0.038 |  |
| 2026-04-06 18:03:49 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 18:03:26 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:03:19 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.113 |  |
| 2026-04-06 18:03:16 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:03:11 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:02:57 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:02:51 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-06 18:02:40 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-06 18:02:36 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.082 |  |
| 2026-04-06 18:02:22 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-04-06 18:02:19 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 18:02:17 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 18:02:08 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-06 18:01:46 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-04-06 18:01:32 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-06 18:01:26 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.079 |  |
| 2026-04-06 18:01:25 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-06 18:01:18 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-04-06 18:01:18 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:00:55 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:00:52 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:00:29 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-04-06 18:00:26 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 17:07:11 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-04-06 18:01:32 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-06 18:02:51 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-06 18:02:40 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-06 18:15:11 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-06 18:02:08 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-06 18:03:49 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 18:02:19 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 18:02:17 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 18:00:52 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:27:52 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:00:26 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:07:35 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:09:01 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:01:18 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:03:26 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:08:24 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:03:11 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:03:16 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:02:22 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:02:57 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:06:02 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:09:01 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:00:55 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:06:42 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-04-06 18:01:18 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-04-06 18:00:29 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-04-06 18:01:25 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-06 18:04:41 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | -0.013 |  |
| 2026-04-06 18:01:46 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-04-06 18:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-04-06 18:05:18 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.030 |  |
| 2026-04-06 18:04:19 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | -0.038 |  |
| 2026-04-06 18:04:37 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | -0.043 |  |
| 2026-04-06 18:01:26 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.079 |  |
| 2026-04-06 18:02:36 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.082 |  |
| 2026-04-06 18:03:19 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.113 |  |
| 2026-04-06 18:04:45 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.126 |  |
| 2026-04-06 18:10:04 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.128 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)