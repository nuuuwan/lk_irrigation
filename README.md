# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--19_11:30:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **77,226 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 11:30:49 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.043 |  |
| 2026-02-19 11:27:25 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:17:17 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.020 |  |
| 2026-02-19 11:14:24 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:13:38 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:12:44 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-19 11:10:12 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-02-19 11:08:17 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:06:30 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:06:25 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:06:06 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:05:21 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-02-19 11:05:03 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.023 |  |
| 2026-02-19 11:04:55 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:04:53 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.029 |  |
| 2026-02-19 11:03:46 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-19 11:03:31 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 11:03:27 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-02-19 11:03:23 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-02-19 11:03:11 | Manampitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | -0.059 |  |
| 2026-02-19 11:03:09 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:03:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.039 |  |
| 2026-02-19 11:03:00 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:02:57 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | -0.059 |  |
| 2026-02-19 11:02:46 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:02:18 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:02:16 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:02:13 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:01:58 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:01:58 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-19 11:01:48 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-02-19 11:01:41 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-02-19 11:01:15 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:01:11 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:01:03 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-02-19 11:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:00:44 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:00:04 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:45:45 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 11:03:27 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-02-19 11:03:23 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-02-19 11:03:46 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-19 11:01:58 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-19 11:10:12 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-02-19 11:03:31 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 11:12:44 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-19 11:00:44 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:27:25 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:03:00 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:00:04 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:08:17 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:06:30 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:02:46 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:02:18 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:02:16 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:06:25 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:13:38 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:01:15 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:05:14 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:06:06 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:03:09 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:02:13 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:01:58 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:04:55 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:14:24 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:01:11 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-19 11:05:21 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-02-19 11:01:41 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-02-19 11:01:48 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-02-19 11:01:03 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-02-19 11:17:17 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.020 |  |
| 2026-02-19 11:05:03 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.023 |  |
| 2026-02-19 11:04:53 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.029 |  |
| 2026-02-19 11:03:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.039 |  |
| 2026-02-19 11:30:49 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.043 |  |
| 2026-02-19 11:03:11 | Manampitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | -0.059 |  |
| 2026-02-19 11:02:57 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)