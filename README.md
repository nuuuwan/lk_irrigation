# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_17:08:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **122,332 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 17:08:56 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:08:11 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:08:03 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | -0.019 |  |
| 2026-04-11 17:07:09 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.030 |  |
| 2026-04-11 17:06:59 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-11 17:06:32 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.011 |  |
| 2026-04-11 17:06:31 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:06:10 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:06:04 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 17:06:02 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.028 |  |
| 2026-04-11 17:05:42 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-11 17:05:23 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | -0.084 |  |
| 2026-04-11 17:04:42 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:04:23 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:04:22 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:03:48 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:03:33 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:03:11 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:03:09 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:02:58 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 17:02:54 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:02:33 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-11 17:02:22 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-04-11 17:01:48 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.100 |  |
| 2026-04-11 17:01:37 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-11 17:01:24 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:01:24 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 17:01:09 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:00:28 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:00:27 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.022 |  |
| 2026-04-11 17:00:25 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:00:15 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:00:09 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:17:43 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.016 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 17:02:33 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-11 17:06:59 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-11 17:01:37 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-11 17:05:42 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-11 17:01:24 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 17:06:04 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 17:02:58 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 17:00:28 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:00:09 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:01:24 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:02:54 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:08:11 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:04:23 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:03:33 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:04:42 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:03:09 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:03:48 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:02:22 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:05:03 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:01:09 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:06:31 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:00:25 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:03:11 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:08:56 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:04:22 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:00:15 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-04-11 17:06:10 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:15:47 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.009 |  |
| 2026-04-11 17:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-04-11 17:06:32 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.011 |  |
| 2026-04-11 16:17:43 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.016 |  |
| 2026-04-11 17:08:03 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | -0.019 |  |
| 2026-04-11 17:00:27 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.022 |  |
| 2026-04-11 17:06:02 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.028 |  |
| 2026-04-11 15:06:43 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.028 |  |
| 2026-04-11 17:07:09 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.030 |  |
| 2026-04-11 17:05:23 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | -0.084 |  |
| 2026-04-11 17:01:48 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)