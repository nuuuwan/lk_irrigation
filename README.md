# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--08_07:10:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **200,414 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-08 07:10:00 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:09:12 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:08:52 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:08:27 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:07:32 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:06:54 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.018 |  |
| 2026-07-08 07:06:47 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:06:36 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-07-08 07:05:50 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-07-08 07:05:29 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | -0.005 |  |
| 2026-07-08 07:05:12 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-07-08 07:04:42 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-08 07:03:59 | Glencourse (Kelani Ganga) | 9.58 | 🟢 Normal | -0.040 |  |
| 2026-07-08 07:03:57 | Hanwella (Kelani Ganga) | 1.33 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-08 07:03:50 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:03:38 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:03:37 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-07-08 07:03:26 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.031 |  |
| 2026-07-08 07:03:23 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -0.009 |  |
| 2026-07-08 07:03:14 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:03:00 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | -0.013 |  |
| 2026-07-08 07:02:49 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.043 |  |
| 2026-07-08 07:02:30 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.042 |  |
| 2026-07-08 07:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | -0.097 |  |
| 2026-07-08 07:02:20 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-08 07:01:57 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:01:50 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-08 07:01:48 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.072 |  |
| 2026-07-08 07:01:17 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:01:10 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:01:07 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:01:04 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-08 07:01:00 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-08 07:00:17 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:00:13 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-08 06:41:07 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-08 07:06:36 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-07-08 07:02:20 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-08 07:05:50 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-07-08 07:03:57 | Hanwella (Kelani Ganga) | 1.33 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-08 07:04:42 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-08 07:01:50 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-08 07:01:00 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-08 07:01:04 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-08 07:06:47 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:00:13 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-08 06:01:27 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:01:07 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:08:52 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:10:00 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:00:17 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:01:17 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:01:57 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:09:12 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:08:27 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-08 06:03:46 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:03:50 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:03:14 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-08 06:02:32 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:07:32 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:03:38 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:05:29 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | -0.005 |  |
| 2026-07-08 06:08:49 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.009 |  |
| 2026-07-08 07:03:23 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -0.009 |  |
| 2026-07-08 07:05:12 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-07-08 07:03:37 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-07-08 07:03:00 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | -0.013 |  |
| 2026-07-08 07:06:54 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.018 |  |
| 2026-07-08 07:03:26 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.031 |  |
| 2026-07-08 07:03:59 | Glencourse (Kelani Ganga) | 9.58 | 🟢 Normal | -0.040 |  |
| 2026-07-08 07:02:30 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.042 |  |
| 2026-07-08 07:02:49 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.043 |  |
| 2026-07-08 07:01:48 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.072 |  |
| 2026-07-08 07:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | -0.097 |  |
| 2026-07-08 06:00:25 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.158 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)