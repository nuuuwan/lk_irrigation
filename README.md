# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_17:12:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **117,900 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 17:12:29 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:10:03 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.324 | 🔺 Rising |
| 2026-04-06 17:08:56 | Peradeniya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-04-06 17:08:54 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-06 17:07:37 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:07:11 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-04-06 17:06:59 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.009 |  |
| 2026-04-06 17:06:49 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:06:47 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-04-06 17:06:29 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:06:25 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:05:47 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-04-06 17:05:18 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:04:19 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-04-06 17:04:17 | Holombuwa (Kelani Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-04-06 17:03:57 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-06 17:03:56 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:03:51 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-04-06 17:03:45 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:03:36 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-04-06 17:03:17 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.030 |  |
| 2026-04-06 17:02:22 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:02:19 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-04-06 17:02:16 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:02:03 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:01:46 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-06 17:01:44 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-04-06 17:01:33 | Wellawaya (Kirindi Oya) | 0.77 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-04-06 17:01:09 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:00:41 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:00:34 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.144 |  |
| 2026-04-06 17:00:31 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-06 17:00:26 | Thanthirimale (Malwathu Oya) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-04-06 17:00:07 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:22:58 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 17:10:03 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.324 | 🔺 Rising |
| 2026-04-06 17:07:11 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-04-06 17:01:33 | Wellawaya (Kirindi Oya) | 0.77 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-04-06 17:01:46 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-06 16:04:55 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-06 17:00:31 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-06 17:03:57 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-06 17:08:54 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-06 17:00:07 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:02:07 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:01:41 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:02:16 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:05:18 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:06:25 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:12:29 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:06:29 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:07:37 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:15:34 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:03:17 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:06:49 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:03:56 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:01:09 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:02:03 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:03:45 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:00:41 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:06:59 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.009 |  |
| 2026-04-06 17:06:47 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-04-06 17:03:51 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-04-06 17:00:26 | Thanthirimale (Malwathu Oya) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-04-06 17:08:56 | Peradeniya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-04-06 17:05:47 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-04-06 17:02:19 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-04-06 16:03:46 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-04-06 17:03:36 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-04-06 17:01:44 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-04-06 17:04:19 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-04-06 17:04:17 | Holombuwa (Kelani Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-04-06 17:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.030 |  |
| 2026-04-06 17:00:34 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.144 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)