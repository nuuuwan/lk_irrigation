# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--13_10:15:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **71,840 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 10:15:40 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-02-13 10:14:24 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -21.252 |  |
| 2026-02-13 10:13:51 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-13 10:13:10 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.009 |  |
| 2026-02-13 10:11:23 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | -0.015 |  |
| 2026-02-13 10:09:14 | Urawa (Nilwala Ganga) | 2.09 | 🟢 Normal | -21.252 |  |
| 2026-02-13 10:09:03 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-13 10:08:45 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.027 |  |
| 2026-02-13 10:08:38 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-13 10:07:53 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.072 |  |
| 2026-02-13 10:05:13 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-13 10:05:10 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-13 10:04:39 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.029 |  |
| 2026-02-13 10:04:24 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-13 10:03:59 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.145 |  |
| 2026-02-13 10:03:51 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-13 10:03:51 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-13 10:03:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.00 | 🟢 Normal | -0.139 |  |
| 2026-02-13 10:03:20 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 10:03:18 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.041 |  |
| 2026-02-13 10:03:18 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 10:03:10 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-13 10:02:42 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-13 10:02:41 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.020 |  |
| 2026-02-13 10:02:23 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 10:02:14 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-13 10:02:05 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-02-13 10:02:05 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-13 10:02:03 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-13 10:01:44 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-02-13 10:01:44 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-13 10:01:38 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-13 10:01:19 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-02-13 10:01:09 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 10:00:30 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-13 10:00:29 | Weraganthota (Mahaweli Ganga) | -1.73 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-02-13 10:00:10 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-13 10:00:06 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-02-13 09:42:24 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.028 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 10:02:05 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-02-13 10:00:29 | Weraganthota (Mahaweli Ganga) | -1.73 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-02-13 10:15:40 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-02-13 10:02:42 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-13 10:03:10 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-13 08:22:31 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-13 10:00:30 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-13 10:03:51 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-13 09:06:17 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-13 10:08:38 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-13 10:04:24 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-13 10:03:20 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 10:01:09 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 10:02:23 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 10:03:18 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 10:01:44 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-13 10:02:14 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-13 10:02:05 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-13 10:05:13 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-13 10:13:51 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-13 10:09:03 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-13 10:02:03 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-13 10:01:19 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-02-13 10:00:10 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-13 10:05:10 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-13 10:03:51 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-13 10:01:38 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-13 10:13:10 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.009 |  |
| 2026-02-13 10:01:44 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-02-13 10:00:06 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-02-13 10:11:23 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | -0.015 |  |
| 2026-02-13 10:02:41 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.020 |  |
| 2026-02-13 10:08:45 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.027 |  |
| 2026-02-13 10:04:39 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.029 |  |
| 2026-02-13 10:03:18 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.041 |  |
| 2026-02-13 10:07:53 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.072 |  |
| 2026-02-13 10:03:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.00 | 🟢 Normal | -0.139 |  |
| 2026-02-13 10:03:59 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.145 |  |
| 2026-02-13 10:14:24 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -21.252 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)