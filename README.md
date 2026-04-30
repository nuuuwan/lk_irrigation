# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_05:22:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **138,808 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 05:22:38 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-04-30 05:20:58 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.075 |  |
| 2026-04-30 05:16:38 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-30 05:16:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | -0.020 |  |
| 2026-04-30 05:15:46 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.073 |  |
| 2026-04-30 05:15:15 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-04-30 05:14:53 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | -0.018 |  |
| 2026-04-30 05:13:50 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.125 |  |
| 2026-04-30 05:13:25 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-04-30 05:12:14 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.026 |  |
| 2026-04-30 05:10:31 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.034 |  |
| 2026-04-30 05:09:08 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | -0.075 |  |
| 2026-04-30 05:08:30 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-30 05:07:38 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-30 05:06:46 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-30 05:06:09 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.011 |  |
| 2026-04-30 05:05:41 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-30 05:05:23 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-30 05:03:36 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-04-30 05:03:34 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.071 |  |
| 2026-04-30 05:03:25 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-30 05:03:23 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-30 05:02:55 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-30 05:02:49 | Horowpothana (Yan Oya) | 1.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-30 05:02:41 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-30 05:02:36 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-30 05:02:35 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-04-30 05:02:17 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-30 05:02:17 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-30 05:01:22 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-30 05:01:21 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-30 05:01:11 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-30 05:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-04-30 05:00:51 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-30 05:00:45 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.086 |  |
| 2026-04-30 05:00:34 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | -0.040 |  |
| 2026-04-30 04:49:51 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.125 |  |
| 2026-04-30 04:45:09 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | -0.075 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 05:15:15 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-04-30 05:02:35 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-04-30 05:22:38 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-04-29 18:03:06 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-30 05:02:49 | Horowpothana (Yan Oya) | 1.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-30 05:03:25 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-30 05:01:22 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-30 05:02:36 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-30 05:05:41 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-30 05:05:23 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-30 05:06:46 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-29 18:03:08 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 05:08:30 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-30 05:01:21 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-30 05:01:11 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-30 05:16:38 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-30 05:07:38 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-30 05:13:25 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-04-30 05:02:41 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-30 05:02:55 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-30 05:02:17 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-30 05:03:23 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-30 05:02:17 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-30 04:08:56 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-30 05:03:36 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-04-30 05:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-04-30 05:06:09 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.011 |  |
| 2026-04-30 05:14:53 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | -0.018 |  |
| 2026-04-30 05:16:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | -0.020 |  |
| 2026-04-30 05:12:14 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.026 |  |
| 2026-04-30 05:10:31 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.034 |  |
| 2026-04-30 05:00:34 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | -0.040 |  |
| 2026-04-29 18:02:02 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.049 |  |
| 2026-04-30 05:03:34 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.071 |  |
| 2026-04-30 05:15:46 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.073 |  |
| 2026-04-30 05:20:58 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.075 |  |
| 2026-04-30 05:09:08 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | -0.075 |  |
| 2026-04-30 05:00:45 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.086 |  |
| 2026-04-30 05:13:50 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.125 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)