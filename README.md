# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--21_20:22:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **79,361 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 20:22:11 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-21 20:18:47 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-21 20:13:48 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-21 20:12:23 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-21 20:11:06 | Pitabeddara (Nilwala Ganga) | 1.57 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-02-21 20:09:52 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-21 20:09:45 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-21 20:08:45 | Manampitiya (Mahaweli Ganga) | 2.11 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-21 20:08:15 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 20:07:58 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-21 20:07:49 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-02-21 20:07:46 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 20:06:42 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.149 |  |
| 2026-02-21 20:05:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | -0.029 |  |
| 2026-02-21 20:05:36 | Rathnapura (Kalu Ganga) | 3.63 | 🟢 Normal | 1.317 | 🔺 Rising |
| 2026-02-21 20:05:11 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-21 20:04:50 | Deraniyagala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-21 20:04:42 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-02-21 20:04:36 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 20:04:27 | Peradeniya (Mahaweli Ganga) | 3.78 | 🟢 Normal | 1.077 | 🔺 Rising |
| 2026-02-21 20:04:24 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 20:03:51 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 20:03:36 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-02-21 20:03:17 | Nakkala (Kumbukkan Oya) | 4.36 | 🟢 Normal | -0.579 |  |
| 2026-02-21 20:03:03 | Dunamale (Aththanagalu Oya) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 20:03:02 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-21 20:02:53 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-21 20:02:32 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-02-21 20:02:26 | Padiyathalawa (Maduru Oya) | 1.33 | 🟢 Normal | -0.021 |  |
| 2026-02-21 20:02:13 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-21 20:02:10 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-02-21 20:02:04 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-21 20:02:02 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-02-21 20:02:01 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 20:01:09 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-21 20:00:40 | Moraketiya (Walawe Ganga) | 1.94 | 🟢 Normal | -0.065 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 20:05:36 | Rathnapura (Kalu Ganga) | 3.63 | 🟢 Normal | 1.317 | 🔺 Rising |
| 2026-02-21 20:04:27 | Peradeniya (Mahaweli Ganga) | 3.78 | 🟢 Normal | 1.077 | 🔺 Rising |
| 2026-02-21 20:11:06 | Pitabeddara (Nilwala Ganga) | 1.57 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-02-21 19:22:19 | Urawa (Nilwala Ganga) | 1.36 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-02-21 20:07:49 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-02-21 20:04:42 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-02-21 20:02:02 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-02-21 20:02:10 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-02-21 20:18:47 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-21 20:02:32 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-02-21 19:04:17 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-02-21 20:07:58 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-21 20:13:48 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-21 20:04:50 | Deraniyagala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-21 20:01:09 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-21 20:08:45 | Manampitiya (Mahaweli Ganga) | 2.11 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-21 20:03:03 | Dunamale (Aththanagalu Oya) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 20:04:36 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 20:04:24 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 20:08:15 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 18:05:22 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 20:03:36 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-02-21 20:02:01 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 20:22:11 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-21 20:07:46 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 20:02:04 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:03:47 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 20:12:23 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-21 20:02:53 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-21 20:02:13 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-21 20:09:52 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-21 20:03:51 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 20:05:11 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:03:01 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | -0.020 |  |
| 2026-02-21 20:02:26 | Padiyathalawa (Maduru Oya) | 1.33 | 🟢 Normal | -0.021 |  |
| 2026-02-21 20:05:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | -0.029 |  |
| 2026-02-21 20:00:40 | Moraketiya (Walawe Ganga) | 1.94 | 🟢 Normal | -0.065 |  |
| 2026-02-21 20:06:42 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.149 |  |
| 2026-02-21 20:03:17 | Nakkala (Kumbukkan Oya) | 4.36 | 🟢 Normal | -0.579 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)