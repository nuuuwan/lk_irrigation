# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--07_17:17:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **66,760 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 17:17:32 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:11:49 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:09:14 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:08:34 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:08:15 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.011 |  |
| 2026-02-07 17:07:31 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:06:50 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:05:55 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-07 17:05:44 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:05:39 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-02-07 17:05:30 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.029 |  |
| 2026-02-07 17:05:12 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:05:09 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:05:01 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-02-07 17:04:19 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:04:09 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:03:57 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.011 |  |
| 2026-02-07 17:03:46 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-02-07 17:03:34 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-02-07 17:03:09 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | -0.020 |  |
| 2026-02-07 17:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.071 |  |
| 2026-02-07 17:02:49 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:02:44 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:02:23 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 17:02:22 | Weraganthota (Mahaweli Ganga) | -2.06 | 🟢 Normal | -0.010 |  |
| 2026-02-07 17:02:20 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 17:02:09 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:01:58 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:01:52 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:01:35 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:01:21 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:01:19 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:01:11 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:00:42 | Manampitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | -0.041 |  |
| 2026-02-07 17:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 17:03:46 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-02-07 17:03:34 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-02-07 16:04:08 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-07 17:05:55 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-07 17:02:20 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 17:02:23 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 17:01:35 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:01:19 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:02:49 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:06:50 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:07:31 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:17:32 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:05:12 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:02:09 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:08:34 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:05:09 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:01:21 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:01:58 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:02:44 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:05:44 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:04:09 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:04:19 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:01:52 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:11:49 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:01:11 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:02:22 | Weraganthota (Mahaweli Ganga) | -2.06 | 🟢 Normal | -0.010 |  |
| 2026-02-07 17:05:01 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-02-07 17:03:57 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.011 |  |
| 2026-02-07 17:08:15 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.011 |  |
| 2026-02-07 17:05:39 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-02-07 17:03:09 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | -0.020 |  |
| 2026-02-07 15:03:28 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.022 |  |
| 2026-02-07 13:11:30 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.026 |  |
| 2026-02-07 17:05:30 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.029 |  |
| 2026-02-07 16:02:47 | Horowpothana (Yan Oya) | 2.52 | 🟢 Normal | -0.037 |  |
| 2026-02-07 17:00:42 | Manampitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | -0.041 |  |
| 2026-02-07 17:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.071 |  |
| 2026-02-07 16:06:26 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | -0.072 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)