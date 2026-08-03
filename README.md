# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--03_11:09:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **223,731 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **4** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 11:09:59 | Magura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.021 |  |
| 2026-08-03 11:09:31 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.025 |  |
| 2026-08-03 11:09:13 | Kithulgala (Kelani Ganga) | 5.90 | 🟠 Minor Flood | 2.908 | 🔺 Rising |
| 2026-08-03 11:07:54 | Rathnapura (Kalu Ganga) | 6.38 | 🟡 Alert | -0.078 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 11:01:55 | Nawalapitiya (Mahaweli Ganga) | 6.50 | 🔴 Major Flood | 1.912 | 🔺 Rising |
| 2026-08-03 11:09:13 | Kithulgala (Kelani Ganga) | 5.90 | 🟠 Minor Flood | 2.908 | 🔺 Rising |
| 2026-08-03 11:04:04 | Norwood (Kelani Ganga) | 3.30 | 🟠 Minor Flood | 0.312 | 🔺 Rising |
| 2026-08-03 11:07:54 | Rathnapura (Kalu Ganga) | 6.38 | 🟡 Alert | -0.078 |  |
| 2026-08-03 11:01:10 | Peradeniya (Mahaweli Ganga) | 6.58 | 🟡 Alert | -0.233 |  |
| 2026-08-03 11:02:58 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | 0.999 | 🔺 Rising |
| 2026-08-03 11:03:38 | Deraniyagala (Kelani Ganga) | 2.68 | 🟢 Normal | 0.737 | 🔺 Rising |
| 2026-08-03 11:03:25 | Hanwella (Kelani Ganga) | 5.11 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-08-03 11:01:28 | Ellagawa (Kalu Ganga) | 7.40 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-08-03 11:05:35 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-03 11:03:14 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-08-03 11:05:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.11 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-08-03 11:05:46 | Panadugama (Nilwala Ganga) | 3.83 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-08-03 11:03:07 | Baddegama (Gin Ganga) | 2.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 11:04:50 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 11:00:12 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-03 11:03:14 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-03 11:01:19 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 11:07:34 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 11:01:33 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-03 11:00:53 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 11:02:52 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-03 11:03:22 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-03 11:07:02 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-03 11:05:31 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-08-03 11:01:14 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 11:02:12 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-03 11:06:41 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-03 11:01:48 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-03 11:04:38 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-08-03 11:01:20 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-08-03 10:02:08 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.020 |  |
| 2026-08-03 11:09:59 | Magura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.021 |  |
| 2026-08-03 11:09:31 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.025 |  |
| 2026-08-03 11:00:27 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.040 |  |
| 2026-08-03 11:05:35 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.049 |  |
| 2026-08-03 11:03:39 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | -0.144 |  |
| 2026-08-03 11:03:50 | Glencourse (Kelani Ganga) | 14.05 | 🟢 Normal | -0.155 |  |
| 2026-08-03 11:02:32 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | -0.325 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)