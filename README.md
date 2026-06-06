# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_23:07:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **172,400 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 23:07:57 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | -0.029 |  |
| 2026-06-06 23:07:32 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-06 23:07:24 | Rathnapura (Kalu Ganga) | 2.72 | 🟢 Normal | -0.057 |  |
| 2026-06-06 23:07:19 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.019 |  |
| 2026-06-06 23:06:38 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-06 23:06:27 | Nawalapitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -2.449 |  |
| 2026-06-06 23:05:59 | Glencourse (Kelani Ganga) | 10.96 | 🟢 Normal | -0.010 |  |
| 2026-06-06 23:05:50 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-06 23:05:45 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-06 23:05:23 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-06 23:05:18 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-06 23:04:40 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-06-06 23:04:39 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.027 |  |
| 2026-06-06 23:04:38 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-06 23:04:37 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-06 23:04:17 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-06-06 23:04:17 | Hanwella (Kelani Ganga) | 3.10 | 🟢 Normal | -0.040 |  |
| 2026-06-06 23:04:00 | Nawalapitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -2.449 |  |
| 2026-06-06 23:03:49 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.088 |  |
| 2026-06-06 23:03:33 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-06 23:03:28 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | 0.000 |  |
| 2026-06-06 23:03:25 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-06-06 23:02:55 | Dunamale (Aththanagalu Oya) | 2.73 | 🟢 Normal | -0.042 |  |
| 2026-06-06 23:02:51 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-06-06 23:01:47 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.092 |  |
| 2026-06-06 23:01:41 | Ellagawa (Kalu Ganga) | 7.15 | 🟢 Normal | -0.010 |  |
| 2026-06-06 23:01:37 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 23:01:27 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.058 |  |
| 2026-06-06 23:01:15 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 23:01:11 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 23:00:49 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:20:34 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | -0.027 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 23:03:33 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-06 22:05:37 | Magura (Kalu Ganga) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 23:01:11 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 23:05:18 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-06 18:06:04 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-06 23:04:38 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-06 23:01:15 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 23:06:38 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-06 23:00:49 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:02:07 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-06 23:05:23 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:04:41 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-06 23:03:28 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | 0.000 |  |
| 2026-06-06 23:01:37 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:07:27 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:00:06 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-06 23:05:45 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:06:58 | Putupaula (Kalu Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-06-06 23:07:32 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:01:43 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-06 23:03:25 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-06-06 23:04:37 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-06 23:05:50 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:06:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-06-06 23:04:17 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-06-06 23:05:59 | Glencourse (Kelani Ganga) | 10.96 | 🟢 Normal | -0.010 |  |
| 2026-06-06 23:01:41 | Ellagawa (Kalu Ganga) | 7.15 | 🟢 Normal | -0.010 |  |
| 2026-06-06 23:02:51 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-06-06 23:04:40 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-06-06 23:07:19 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.019 |  |
| 2026-06-06 23:04:39 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.027 |  |
| 2026-06-06 23:07:57 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | -0.029 |  |
| 2026-06-06 23:04:17 | Hanwella (Kelani Ganga) | 3.10 | 🟢 Normal | -0.040 |  |
| 2026-06-06 23:02:55 | Dunamale (Aththanagalu Oya) | 2.73 | 🟢 Normal | -0.042 |  |
| 2026-06-06 23:07:24 | Rathnapura (Kalu Ganga) | 2.72 | 🟢 Normal | -0.057 |  |
| 2026-06-06 23:01:27 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.058 |  |
| 2026-06-06 23:03:49 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.088 |  |
| 2026-06-06 23:01:47 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.092 |  |
| 2026-06-06 23:06:27 | Nawalapitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -2.449 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)