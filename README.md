# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--25_18:20:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **82,896 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 18:20:33 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:16:46 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:12:51 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-25 18:11:37 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:07:16 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:07:07 | Dunamale (Aththanagalu Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:06:11 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:06:02 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-25 18:05:13 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | -0.009 |  |
| 2026-02-25 18:04:50 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.031 |  |
| 2026-02-25 18:04:30 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-02-25 18:04:22 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:04:22 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 18:03:21 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-02-25 18:03:19 | Thawalama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:03:17 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:03:17 | Thawalama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:03:08 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:02:55 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:02:51 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-02-25 18:02:37 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-02-25 18:02:19 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:02:19 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-02-25 18:02:19 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.030 |  |
| 2026-02-25 18:02:05 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-02-25 18:02:00 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-02-25 18:01:56 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-02-25 18:01:50 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.081 |  |
| 2026-02-25 18:01:40 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:01:37 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:01:35 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:01:31 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-02-25 18:01:21 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-02-25 18:00:34 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:00:34 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-02-25 18:00:27 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 18:00:11 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 18:01:56 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-02-25 18:12:51 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-25 18:06:02 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-25 18:00:27 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 18:04:22 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 18:02:55 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:01:40 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:01:37 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:04:22 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:20:33 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:01:35 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:11:21 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:02:45 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:03:08 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:03:17 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:07:07 | Dunamale (Aththanagalu Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:02:19 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:02:19 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:11:37 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:07:16 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:03:19 | Thawalama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:06:11 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:16:46 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:00:34 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:05:13 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | -0.009 |  |
| 2026-02-25 18:04:30 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-02-25 18:02:19 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-02-25 18:03:21 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-02-25 18:02:05 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-02-25 18:01:21 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-02-25 18:00:34 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-02-25 18:01:31 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-02-25 18:02:51 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-02-25 18:00:11 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-02-25 18:02:00 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-02-25 18:02:37 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-02-25 18:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.030 |  |
| 2026-02-25 18:04:50 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.031 |  |
| 2026-02-25 18:01:50 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)