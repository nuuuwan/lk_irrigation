# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_23:02:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **127,009 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 23:02:51 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.041 |  |
| 2026-04-16 23:02:50 | Peradeniya (Mahaweli Ganga) | 1.71 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-04-16 23:02:47 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-04-16 23:02:39 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-16 23:02:36 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-16 23:02:36 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.075 |  |
| 2026-04-16 23:02:23 | Ellagawa (Kalu Ganga) | 4.59 | 🟢 Normal | -0.050 |  |
| 2026-04-16 23:02:21 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-04-16 23:02:16 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-16 23:02:15 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-04-16 23:02:10 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-16 23:02:07 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-16 23:01:42 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-04-16 23:01:37 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 23:01:17 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-16 23:01:00 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-16 23:00:46 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-16 23:00:43 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-04-16 23:00:40 | Glencourse (Kelani Ganga) | 9.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-16 22:44:32 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.006 |  |
| 2026-04-16 22:18:42 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | -0.018 |  |
| 2026-04-16 22:14:35 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.075 |  |
| 2026-04-16 22:12:18 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.062 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 23:02:50 | Peradeniya (Mahaweli Ganga) | 1.71 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-04-16 23:01:42 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-04-16 23:02:07 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-16 23:00:40 | Glencourse (Kelani Ganga) | 9.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-16 22:08:45 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-16 22:03:00 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-16 22:01:39 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-16 23:01:37 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 23:01:00 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:00:19 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-16 23:01:17 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-16 23:00:46 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-16 22:02:54 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-16 22:02:31 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 23:02:39 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-16 23:02:36 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-16 23:02:15 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:00:56 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-04-16 22:07:24 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-16 22:07:45 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-04-16 22:04:22 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-16 22:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-16 22:44:32 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.006 |  |
| 2026-04-16 22:03:58 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-16 23:00:43 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-04-16 22:02:29 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-04-16 23:02:16 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-16 23:02:10 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-16 23:02:47 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-04-16 22:18:42 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | -0.018 |  |
| 2026-04-16 23:02:21 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-04-16 22:04:53 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-04-16 22:03:59 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-04-16 22:05:23 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.029 |  |
| 2026-04-16 23:02:51 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.041 |  |
| 2026-04-16 23:02:23 | Ellagawa (Kalu Ganga) | 4.59 | 🟢 Normal | -0.050 |  |
| 2026-04-16 22:12:18 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.062 |  |
| 2026-04-16 23:02:36 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.075 |  |
| 2026-04-16 18:00:37 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | -4.696 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)