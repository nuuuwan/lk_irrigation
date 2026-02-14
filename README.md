# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--15_01:06:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **73,289 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 01:06:30 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-02-15 01:05:45 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-15 01:05:25 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-15 01:05:05 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-02-15 01:04:59 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-15 01:04:18 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-02-15 01:04:13 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 01:03:18 | Glencourse (Kelani Ganga) | 8.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 01:03:04 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-15 01:03:01 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-15 01:02:47 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-02-15 01:02:33 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 01:02:12 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-15 01:02:02 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-15 01:01:52 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-15 01:01:26 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-15 01:01:25 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 01:01:24 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.103 |  |
| 2026-02-15 01:01:12 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-15 01:01:09 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-15 00:17:47 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.283 |  |
| 2026-02-15 00:12:31 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-15 00:10:59 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-02-15 00:10:54 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.052 |  |
| 2026-02-15 00:09:58 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-02-15 00:09:44 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 00:10:59 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-02-15 00:07:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-02-15 00:00:48 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-02-15 00:09:58 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-02-15 01:03:01 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-15 01:05:45 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-15 00:07:32 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-15 01:05:25 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-15 01:03:18 | Glencourse (Kelani Ganga) | 8.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 01:01:25 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 01:04:13 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 22:00:48 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 18:02:04 | Weraganthota (Mahaweli Ganga) | -1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 01:04:18 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-02-15 00:01:54 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-15 01:02:02 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-15 00:03:20 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-15 00:02:16 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-15 01:02:12 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:03:27 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:03:21 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-15 01:04:59 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-15 01:02:47 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-02-15 01:06:30 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-02-15 00:04:56 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-15 01:02:33 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 01:01:12 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-15 01:01:09 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-15 01:01:26 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:01:28 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-02-15 01:03:04 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-15 01:01:52 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-15 01:05:05 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-02-15 00:05:36 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-02-15 00:01:27 | Padiyathalawa (Maduru Oya) | 1.60 | 🟢 Normal | -0.050 |  |
| 2026-02-15 00:10:54 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.052 |  |
| 2026-02-15 01:01:24 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.103 |  |
| 2026-02-15 00:17:47 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.283 |  |
| 2026-02-15 00:02:12 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -3.130 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)