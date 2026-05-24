# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--24_06:33:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **160,272 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-24 06:33:04 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:26:16 | Dunamale (Aththanagalu Oya) | 4.05 | 🟡 Alert | -0.043 |  |
| 2026-05-24 06:24:06 | Peradeniya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.029 |  |
| 2026-05-24 06:11:34 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:11:15 | Ellagawa (Kalu Ganga) | 10.10 | 🟡 Alert | -0.036 |  |
| 2026-05-24 06:10:43 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | -0.048 |  |
| 2026-05-24 06:10:25 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:09:58 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:08:57 | Putupaula (Kalu Ganga) | 3.30 | 🟡 Alert | 0.000 |  |
| 2026-05-24 06:06:00 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.014 |  |
| 2026-05-24 06:05:37 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:05:29 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:05:22 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.050 |  |
| 2026-05-24 06:04:48 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | -0.030 |  |
| 2026-05-24 06:04:34 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:04:17 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-05-24 06:03:54 | Glencourse (Kelani Ganga) | 10.96 | 🟢 Normal | -0.107 |  |
| 2026-05-24 06:03:50 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-05-24 06:03:38 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:03:34 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.021 |  |
| 2026-05-24 06:03:29 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-05-24 06:03:24 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:03:18 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:03:11 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:02:54 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.010 |  |
| 2026-05-24 06:02:50 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:02:27 | Hanwella (Kelani Ganga) | 4.97 | 🟢 Normal | -0.090 |  |
| 2026-05-24 06:02:11 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:02:05 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-24 06:02:00 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-05-24 06:01:58 | Magura (Kalu Ganga) | 2.52 | 🟢 Normal | -0.049 |  |
| 2026-05-24 06:01:26 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:01:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.61 | 🟠 Minor Flood | -0.064 |  |
| 2026-05-24 06:01:01 | Rathnapura (Kalu Ganga) | 4.69 | 🟢 Normal | -0.082 |  |
| 2026-05-24 06:00:52 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-24 06:00:28 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:00:20 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:00:17 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-24 05:59:54 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-24 06:01:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.61 | 🟠 Minor Flood | -0.064 |  |
| 2026-05-24 06:08:57 | Putupaula (Kalu Ganga) | 3.30 | 🟡 Alert | 0.000 |  |
| 2026-05-24 06:11:15 | Ellagawa (Kalu Ganga) | 10.10 | 🟡 Alert | -0.036 |  |
| 2026-05-24 06:26:16 | Dunamale (Aththanagalu Oya) | 4.05 | 🟡 Alert | -0.043 |  |
| 2026-05-24 06:02:05 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-24 06:00:17 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-24 06:00:52 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-24 05:59:54 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:03:24 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:03:38 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:04:34 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:01:26 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:00:20 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:33:04 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:00:28 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:03:18 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:05:29 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:11:34 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:05:37 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:03:11 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:10:25 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-24 06:02:11 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-24 05:10:41 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-05-24 06:03:50 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-05-24 06:03:29 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-05-24 06:02:54 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.010 |  |
| 2026-05-23 18:01:26 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-05-24 06:04:17 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-05-24 06:06:00 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.014 |  |
| 2026-05-24 06:02:00 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-05-24 06:03:34 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.021 |  |
| 2026-05-24 06:24:06 | Peradeniya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.029 |  |
| 2026-05-24 06:04:48 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | -0.030 |  |
| 2026-05-24 06:10:43 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | -0.048 |  |
| 2026-05-24 06:01:58 | Magura (Kalu Ganga) | 2.52 | 🟢 Normal | -0.049 |  |
| 2026-05-24 06:05:22 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.050 |  |
| 2026-05-24 06:01:01 | Rathnapura (Kalu Ganga) | 4.69 | 🟢 Normal | -0.082 |  |
| 2026-05-24 06:02:27 | Hanwella (Kelani Ganga) | 4.97 | 🟢 Normal | -0.090 |  |
| 2026-05-24 06:03:54 | Glencourse (Kelani Ganga) | 10.96 | 🟢 Normal | -0.107 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)