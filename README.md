# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--11_07:00:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **42,435 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 07:00:37 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:00:36 | Horowpothana (Yan Oya) | 2.61 | 🟢 Normal | -0.011 |  |
| 2026-01-11 07:00:07 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-11 06:38:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 15.429 | 🔺 Rising |
| 2026-01-11 06:38:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.61 | 🟢 Normal | 15.429 | 🔺 Rising |
| 2026-01-11 06:35:58 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-11 06:18:09 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-11 06:14:41 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-11 06:14:39 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-11 06:11:21 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-11 06:10:56 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.010 |  |
| 2026-01-11 06:10:40 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.047 |  |
| 2026-01-11 06:10:33 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.018 |  |
| 2026-01-11 06:07:16 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.082 |  |
| 2026-01-11 06:06:10 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.012 |  |
| 2026-01-11 06:05:37 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-11 06:04:58 | Horowpothana (Yan Oya) | 2.62 | 🟢 Normal | -0.011 |  |
| 2026-01-11 06:04:56 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-11 06:04:35 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 06:04:33 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-11 06:04:19 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.021 |  |
| 2026-01-11 06:03:56 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-11 06:03:29 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-11 06:03:29 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 06:03:21 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-11 06:03:08 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.020 |  |
| 2026-01-11 06:02:59 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 06:38:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 15.429 | 🔺 Rising |
| 2026-01-11 06:11:21 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-11 06:00:37 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-11 06:04:56 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-11 06:03:56 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-11 06:02:17 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 06:03:29 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 06:04:35 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 06:00:47 | Weraganthota (Mahaweli Ganga) | -1.38 | 🟢 Normal | 0.002 |  |
| 2026-01-11 06:00:59 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-11 06:01:41 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:00:37 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 06:02:18 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-11 06:04:33 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-11 06:03:29 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-11 06:35:58 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-11 05:59:29 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-11 06:02:44 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-11 06:05:37 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-11 06:02:28 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-01-11 06:18:09 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-11 06:00:31 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:00:07 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-11 06:14:41 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:01:35 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-11 06:00:37 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-11 05:08:30 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-01-11 06:10:56 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.010 |  |
| 2026-01-11 06:03:21 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-11 06:01:22 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-01-11 07:00:36 | Horowpothana (Yan Oya) | 2.61 | 🟢 Normal | -0.011 |  |
| 2026-01-11 06:06:10 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.012 |  |
| 2026-01-11 06:10:33 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.018 |  |
| 2026-01-11 06:03:08 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.020 |  |
| 2026-01-11 06:04:19 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.021 |  |
| 2026-01-11 06:02:58 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.035 |  |
| 2026-01-11 06:10:40 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.047 |  |
| 2026-01-11 06:02:13 | Manampitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.049 |  |
| 2026-01-11 06:07:16 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.082 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)