# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--12_14:15:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **71,101 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 14:15:01 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:12:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 14:11:44 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:11:28 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:11:11 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:10:00 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:09:58 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:09:01 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:09:00 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.009 |  |
| 2026-02-12 14:06:53 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:06:37 | Thawalama (Gin Ganga) | 0.94 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-12 14:06:02 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-12 14:04:45 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-12 14:04:42 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:04:19 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:03:59 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-02-12 14:03:55 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:03:46 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-02-12 14:03:31 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:03:08 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:02:58 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:02:45 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | -0.029 |  |
| 2026-02-12 14:02:19 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:02:14 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.030 |  |
| 2026-02-12 14:02:11 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:02:08 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.200 |  |
| 2026-02-12 14:02:08 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-02-12 14:02:02 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-02-12 14:02:02 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-12 14:02:01 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:01:30 | Dunamale (Aththanagalu Oya) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 14:01:13 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | -0.022 |  |
| 2026-02-12 14:01:01 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:00:51 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-02-12 14:00:40 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:00:15 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:00:09 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.052 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 13:02:25 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-02-12 14:04:45 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-12 14:00:09 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-12 14:06:37 | Thawalama (Gin Ganga) | 0.94 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-12 14:06:02 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-12 14:03:46 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-02-12 13:02:35 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-12 14:02:02 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-12 14:01:30 | Dunamale (Aththanagalu Oya) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 14:12:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 14:02:01 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:00:15 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:02:11 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:00:40 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:02:19 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:03:55 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:01:01 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:11:11 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:10:00 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:02:58 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:03:31 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:03:08 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:04:19 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 13:04:36 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:11:44 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:09:01 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:06:53 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-12 13:05:56 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:04:42 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:15:01 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:09:00 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.009 |  |
| 2026-02-12 14:00:51 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-02-12 14:03:59 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-02-12 14:02:08 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-02-12 14:02:02 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-02-12 14:01:13 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | -0.022 |  |
| 2026-02-12 14:02:45 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | -0.029 |  |
| 2026-02-12 14:02:14 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.030 |  |
| 2026-02-12 14:02:08 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.200 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)