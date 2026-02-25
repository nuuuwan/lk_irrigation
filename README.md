# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--25_13:05:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **82,690 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 13:05:07 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-25 13:04:52 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-25 13:04:34 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | -0.030 |  |
| 2026-02-25 13:04:23 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-25 13:04:15 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-02-25 13:03:37 | Manampitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-25 13:03:19 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-25 13:03:14 | Dunamale (Aththanagalu Oya) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-02-25 13:02:55 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.059 |  |
| 2026-02-25 13:02:44 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-02-25 13:02:31 | Putupaula (Kalu Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-25 13:02:26 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 13:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 13:02:23 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-02-25 13:02:21 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-02-25 13:02:08 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.005 |  |
| 2026-02-25 13:02:08 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-25 13:01:58 | Weraganthota (Mahaweli Ganga) | -1.70 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-02-25 13:01:51 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-25 13:01:49 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-25 13:01:40 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-25 13:01:34 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-25 13:01:34 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.031 |  |
| 2026-02-25 13:01:19 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-25 13:01:15 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | -0.010 |  |
| 2026-02-25 13:01:13 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-25 13:01:07 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:58:06 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:09:14 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 13:01:58 | Weraganthota (Mahaweli Ganga) | -1.70 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-02-25 13:02:08 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-25 13:03:37 | Manampitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-25 12:05:44 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-25 13:01:34 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-25 13:01:51 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-25 13:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 12:02:06 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 13:02:26 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 13:01:19 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-25 13:01:13 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:58:06 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-25 13:01:49 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-25 13:04:52 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:05:04 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:09:14 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-25 13:04:23 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-25 13:03:19 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:02:35 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-25 13:01:07 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-25 13:02:31 | Putupaula (Kalu Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:04:44 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:04:34 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-25 13:05:07 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:04:18 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-25 13:02:08 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.005 |  |
| 2026-02-25 13:03:14 | Dunamale (Aththanagalu Oya) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-02-25 13:04:15 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-02-25 13:01:40 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-25 13:02:21 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-02-25 12:06:22 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-02-25 13:02:23 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-02-25 13:01:15 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | -0.010 |  |
| 2026-02-25 13:02:44 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-02-25 13:04:34 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | -0.030 |  |
| 2026-02-25 13:01:34 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.031 |  |
| 2026-02-25 12:00:20 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.033 |  |
| 2026-02-25 12:04:49 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | -0.035 |  |
| 2026-02-25 13:02:55 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)