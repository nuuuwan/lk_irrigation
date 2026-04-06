# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--07_01:22:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **118,176 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 01:22:06 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-07 01:16:57 | Panadugama (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-04-07 01:12:49 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-07 01:12:04 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -36.000 |  |
| 2026-04-07 01:12:03 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -36.000 |  |
| 2026-04-07 01:07:35 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | -0.029 |  |
| 2026-04-07 01:07:15 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-04-07 01:06:12 | Kithulgala (Kelani Ganga) | 1.27 | 🟢 Normal | -0.285 |  |
| 2026-04-07 01:06:09 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-07 01:05:51 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.050 |  |
| 2026-04-07 01:05:25 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 01:04:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-07 01:03:42 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.080 |  |
| 2026-04-07 01:03:24 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-07 01:02:52 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-04-07 01:02:36 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-07 01:02:10 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.010 |  |
| 2026-04-07 01:02:00 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-07 01:01:59 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-07 01:01:15 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-04-07 01:01:10 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-07 01:00:48 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-07 01:00:28 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-07 01:00:19 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-07 01:00:12 | Peradeniya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.100 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 01:07:15 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-04-07 01:02:52 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-04-07 01:04:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-07 00:05:23 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-07 00:06:35 | Putupaula (Kalu Ganga) | 0.26 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-07 01:03:24 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-07 00:05:37 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-07 00:01:35 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 01:05:25 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 01:22:06 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-07 01:00:19 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-07 00:02:47 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-07 01:00:28 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-06 23:01:39 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-07 01:01:10 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:00:26 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-07 01:02:36 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-06 23:03:17 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-07 01:01:15 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-04-07 01:16:57 | Panadugama (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-04-07 01:01:59 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-06 23:02:35 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-07 00:01:39 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-07 01:00:48 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-07 01:06:09 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-07 01:02:00 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-07 00:03:04 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-07 01:12:49 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-07 01:02:10 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.010 |  |
| 2026-04-06 18:01:18 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-04-07 01:07:35 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | -0.029 |  |
| 2026-04-07 00:06:53 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.029 |  |
| 2026-04-07 00:07:56 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.042 |  |
| 2026-04-07 01:05:51 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.050 |  |
| 2026-04-06 18:01:26 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.079 |  |
| 2026-04-07 01:03:42 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.080 |  |
| 2026-04-07 01:00:12 | Peradeniya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.100 |  |
| 2026-04-07 01:06:12 | Kithulgala (Kelani Ganga) | 1.27 | 🟢 Normal | -0.285 |  |
| 2026-04-07 01:12:04 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)