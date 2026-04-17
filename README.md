# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_05:12:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **128,101 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-18 05:12:58 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-18 05:11:26 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-04-18 05:10:41 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-18 05:08:12 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | -0.009 |  |
| 2026-04-18 05:07:49 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | -0.005 |  |
| 2026-04-18 05:07:46 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 05:07:07 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.033 |  |
| 2026-04-18 05:06:27 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.153 |  |
| 2026-04-18 05:06:21 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-18 05:05:35 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-04-18 05:04:11 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-18 05:04:10 | Kithulgala (Kelani Ganga) | 1.22 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-18 05:03:58 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 05:03:21 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | -0.025 |  |
| 2026-04-18 05:03:11 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-18 05:02:58 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-18 05:02:47 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-04-18 05:02:29 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-18 05:02:13 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 05:02:00 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-04-18 05:01:38 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-18 05:01:34 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-18 05:01:16 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-18 05:01:14 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.079 |  |
| 2026-04-18 05:01:04 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.011 |  |
| 2026-04-18 05:00:54 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-18 05:00:52 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | -0.010 |  |
| 2026-04-18 05:00:18 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-18 05:00:17 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-18 04:53:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 8.308 | 🔺 Rising |
| 2026-04-18 04:53:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | 8.308 | 🔺 Rising |
| 2026-04-18 04:51:46 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-18 04:36:02 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-18 04:35:19 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-18 04:35:17 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-18 04:33:34 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-18 04:32:51 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-18 04:30:13 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.033 |  |
| 2026-04-18 04:28:25 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-18 04:53:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 8.308 | 🔺 Rising |
| 2026-04-18 04:00:25 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-04-18 04:01:57 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-18 05:00:17 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-18 05:04:10 | Kithulgala (Kelani Ganga) | 1.22 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-18 05:00:18 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-18 05:00:54 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-18 05:06:21 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-18 04:06:02 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-04-18 04:06:52 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 18:04:21 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.000 |  |
| 2026-04-18 05:02:58 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-18 05:01:38 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:02:55 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-18 05:07:46 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 04:03:25 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-18 05:10:41 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-18 05:01:16 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:04:03 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-18 05:02:13 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 05:03:58 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 05:01:34 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-18 05:03:11 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:00:41 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-04-18 05:12:58 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-18 05:02:29 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-18 05:07:49 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | -0.005 |  |
| 2026-04-18 04:08:27 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | -0.005 |  |
| 2026-04-18 05:08:12 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | -0.009 |  |
| 2026-04-18 05:11:26 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-04-18 05:02:47 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-04-18 05:05:35 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-04-18 05:00:52 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | -0.010 |  |
| 2026-04-18 05:02:00 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-04-18 05:01:04 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.011 |  |
| 2026-04-18 05:03:21 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | -0.025 |  |
| 2026-04-18 05:07:07 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.033 |  |
| 2026-04-18 05:01:14 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.079 |  |
| 2026-04-18 05:06:27 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.153 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)