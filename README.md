# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--03_13:02:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **169,319 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-03 13:02:35 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-03 13:02:29 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 13:02:20 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-03 13:02:12 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-06-03 13:01:56 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-03 13:01:51 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-03 13:01:50 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-03 13:01:35 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-03 13:01:31 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-03 13:01:30 | Ellagawa (Kalu Ganga) | 5.36 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-06-03 13:01:26 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-03 13:01:10 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-06-03 13:01:08 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-03 13:00:53 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-03 13:00:50 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-03 13:00:46 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-06-03 13:00:29 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 12:58:13 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-03 13:01:30 | Ellagawa (Kalu Ganga) | 5.36 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-06-03 12:03:23 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-03 13:01:51 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-03 13:01:35 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-03 13:00:50 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-03 12:02:38 | Glencourse (Kelani Ganga) | 9.81 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-03 12:02:46 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-03 12:06:45 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 13:02:29 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 12:02:54 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 12:03:43 | Dunamale (Aththanagalu Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 12:03:13 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-06-03 13:00:29 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 13:01:31 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-03 12:01:12 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-03 13:01:56 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-03 13:01:26 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-03 13:01:08 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-03 12:05:03 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 12:02:42 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-03 13:02:35 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-03 13:01:10 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-06-03 12:08:09 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-03 13:02:20 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-03 12:02:32 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-03 12:03:46 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-06-03 12:06:53 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-03 12:03:05 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-03 13:00:53 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-03 13:01:50 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-03 12:07:00 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.009 |  |
| 2026-06-03 12:04:53 | Hanwella (Kelani Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-06-03 12:04:03 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-06-03 13:02:12 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-06-03 13:00:46 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-06-03 12:58:13 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-06-03 12:03:18 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-06-03 12:04:14 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.029 |  |
| 2026-06-03 12:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | -0.058 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)