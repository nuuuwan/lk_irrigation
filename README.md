# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--21_11:23:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **212,174 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-21 11:23:27 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:08:07 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:07:48 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | -0.060 |  |
| 2026-07-21 11:07:45 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.196 |  |
| 2026-07-21 11:07:31 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:07:25 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-07-21 11:07:01 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:06:27 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-21 11:06:25 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.104 |  |
| 2026-07-21 11:05:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | -0.059 |  |
| 2026-07-21 11:05:57 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:05:10 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:04:53 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:04:48 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:04:26 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:04:25 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-07-21 11:03:55 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:03:42 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:03:26 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-21 11:03:24 | Hanwella (Kelani Ganga) | 0.85 | 🟢 Normal | -0.040 |  |
| 2026-07-21 11:03:23 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:02:49 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.117 |  |
| 2026-07-21 11:02:47 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.132 |  |
| 2026-07-21 11:02:23 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | -0.010 |  |
| 2026-07-21 11:02:10 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-21 11:02:08 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-07-21 11:01:57 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-07-21 11:01:52 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:01:52 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:01:42 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:01:33 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-21 11:01:25 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:01:25 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:01:06 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:01:00 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:00:47 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:00:42 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:00:37 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-21 11:00:09 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-21 10:59:49 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-21 11:02:10 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-21 11:03:26 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-21 11:00:37 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-21 11:01:33 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-21 11:06:27 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-21 11:01:42 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:01:00 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:04:48 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:01:52 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:04:53 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:04:26 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:03:23 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:05:57 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:01:25 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:01:25 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:03:55 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:07:31 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:00:09 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:01:52 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:03:42 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:00:47 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:05:10 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:07:01 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:08:07 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:23:27 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:00:42 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:01:06 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-21 11:02:08 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-07-21 11:02:23 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | -0.010 |  |
| 2026-07-21 11:04:25 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-07-21 11:07:25 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-07-21 11:01:57 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-07-21 11:03:24 | Hanwella (Kelani Ganga) | 0.85 | 🟢 Normal | -0.040 |  |
| 2026-07-21 11:05:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | -0.059 |  |
| 2026-07-21 11:07:48 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | -0.060 |  |
| 2026-07-21 11:06:25 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.104 |  |
| 2026-07-21 11:02:49 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.117 |  |
| 2026-07-21 11:02:47 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.132 |  |
| 2026-07-21 11:07:45 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.196 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)