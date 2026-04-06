# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_23:00:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **118,085 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 23:00:42 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-06 23:00:35 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-06 22:33:29 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-04-06 22:18:43 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-06 22:15:33 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-06 22:12:51 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.128 |  |
| 2026-04-06 22:11:02 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-06 22:10:36 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-06 22:10:23 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-04-06 22:07:40 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-06 22:07:32 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-06 22:07:25 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.029 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 22:02:37 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-04-06 22:01:15 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-04-06 22:03:25 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-06 22:06:11 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-06 22:04:01 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-06 22:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-06 23:00:42 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-06 22:04:13 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-06 21:02:21 | Manampitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-06 22:03:28 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 22:02:56 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 22:00:35 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 22:33:29 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-04-06 22:04:28 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-06 22:01:31 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-06 23:00:35 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:00:26 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-06 22:06:12 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-06 22:07:40 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-06 22:07:32 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-06 22:10:23 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-04-06 22:00:29 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-06 22:02:33 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-06 22:01:25 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-06 22:15:33 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-06 22:10:36 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-06 22:11:02 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-06 22:04:51 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-06 22:01:31 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-06 22:01:59 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:01:18 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-04-06 22:05:25 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-04-06 22:01:45 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-04-06 22:01:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | -0.013 |  |
| 2026-04-06 22:01:01 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.021 |  |
| 2026-04-06 22:07:25 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.029 |  |
| 2026-04-06 22:05:37 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.054 |  |
| 2026-04-06 18:01:26 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.079 |  |
| 2026-04-06 22:12:51 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.128 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)