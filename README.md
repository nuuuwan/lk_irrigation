# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--05_20:03:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **65,027 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-05 20:03:40 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-02-05 20:03:38 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-05 20:03:29 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-05 20:03:24 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-05 20:03:15 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-05 20:03:00 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.042 |  |
| 2026-02-05 20:02:40 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.060 |  |
| 2026-02-05 20:02:33 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-02-05 20:02:22 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-02-05 20:02:13 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-02-05 20:02:05 | Siyambalanduwa (Heda Oya) | 1.23 | 🟢 Normal | -0.030 |  |
| 2026-02-05 20:02:02 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-05 20:01:39 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-05 20:01:37 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-05 20:01:33 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-05 20:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-05 19:31:24 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-05 19:24:55 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-05 19:17:33 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-05 19:17:01 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-02-05 19:15:08 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.042 |  |
| 2026-02-05 19:11:14 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-05 19:11:14 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.018 |  |
| 2026-02-05 19:08:27 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-05 19:02:18 | Peradeniya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-02-05 20:03:40 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-02-05 20:02:33 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-05 19:05:27 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-05 20:02:22 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-02-05 06:07:34 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-05 20:03:29 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-05 20:03:38 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-05 19:03:52 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 19:11:14 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-05 20:01:33 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-05 20:01:37 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-05 20:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-05 20:03:24 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-05 19:31:24 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-05 19:03:28 | Padiyathalawa (Maduru Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-02-05 20:01:39 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-05 19:05:19 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-05 20:03:15 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-05 18:04:13 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-05 19:24:55 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-05 19:17:33 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-05 19:01:37 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-02-05 20:02:02 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-05 18:05:46 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-02-05 19:11:14 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.018 |  |
| 2026-02-05 19:05:23 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.020 |  |
| 2026-02-05 20:02:13 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-02-05 20:02:05 | Siyambalanduwa (Heda Oya) | 1.23 | 🟢 Normal | -0.030 |  |
| 2026-02-05 19:08:27 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | -0.040 |  |
| 2026-02-05 20:03:00 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.042 |  |
| 2026-02-05 19:15:08 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.042 |  |
| 2026-02-05 18:05:45 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | -0.046 |  |
| 2026-02-05 20:02:40 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.060 |  |
| 2026-02-05 19:04:16 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.067 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)