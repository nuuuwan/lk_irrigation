# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_00:14:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **222,444 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 00:14:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.37 | 🟢 Normal | 1.241 | 🔺 Rising |
| 2026-08-02 00:13:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.36 | 🟢 Normal | 1.241 | 🔺 Rising |
| 2026-08-02 00:13:18 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.088 |  |
| 2026-08-02 00:13:05 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:12:23 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-02 00:11:42 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:11:29 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:10:40 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:08:51 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:08:22 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.009 |  |
| 2026-08-02 00:07:33 | Rathnapura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.130 |  |
| 2026-08-02 00:06:49 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-08-02 00:06:44 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:06:03 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.113 |  |
| 2026-08-02 00:05:51 | Hanwella (Kelani Ganga) | 4.52 | 🟢 Normal | -0.170 |  |
| 2026-08-02 00:05:45 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | -0.109 |  |
| 2026-08-02 00:05:42 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.029 |  |
| 2026-08-02 00:05:41 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | -0.251 |  |
| 2026-08-02 00:05:35 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:05:21 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:05:02 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 00:04:57 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:03:47 | Nawalapitiya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.030 |  |
| 2026-08-02 00:03:31 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-08-02 00:03:12 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:02:55 | Peradeniya (Mahaweli Ganga) | 3.26 | 🟢 Normal | -0.041 |  |
| 2026-08-02 00:02:46 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:02:42 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | -0.081 |  |
| 2026-08-02 00:02:40 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.032 |  |
| 2026-08-02 00:02:37 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | -0.100 |  |
| 2026-08-02 00:02:11 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:01:24 | Ellagawa (Kalu Ganga) | 6.99 | 🟢 Normal | -0.053 |  |
| 2026-08-02 00:01:19 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:01:13 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:00:38 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.032 |  |
| 2026-08-02 00:00:19 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 00:14:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.37 | 🟢 Normal | 1.241 | 🔺 Rising |
| 2026-08-01 23:18:00 | Putupaula (Kalu Ganga) | 1.49 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-08-02 00:05:02 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 18:03:08 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 00:12:23 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-02 00:11:29 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:04:57 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-01 23:01:03 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:03:57 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:06:44 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:11:42 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:01:13 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:13:05 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:08:51 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:02:11 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:02:46 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:10:40 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:05:35 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-01 23:39:08 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:03:12 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:05:21 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:08:22 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.009 |  |
| 2026-08-02 00:03:31 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-08-02 00:06:49 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-08-02 00:05:42 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.029 |  |
| 2026-08-02 00:03:47 | Nawalapitiya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.030 |  |
| 2026-08-02 00:00:38 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.032 |  |
| 2026-08-02 00:02:40 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.032 |  |
| 2026-08-02 00:02:55 | Peradeniya (Mahaweli Ganga) | 3.26 | 🟢 Normal | -0.041 |  |
| 2026-08-01 18:00:26 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.042 |  |
| 2026-08-02 00:01:24 | Ellagawa (Kalu Ganga) | 6.99 | 🟢 Normal | -0.053 |  |
| 2026-08-02 00:02:42 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | -0.081 |  |
| 2026-08-02 00:13:18 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.088 |  |
| 2026-08-02 00:02:37 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | -0.100 |  |
| 2026-08-02 00:05:45 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | -0.109 |  |
| 2026-08-02 00:06:03 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.113 |  |
| 2026-08-02 00:07:33 | Rathnapura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.130 |  |
| 2026-08-02 00:05:51 | Hanwella (Kelani Ganga) | 4.52 | 🟢 Normal | -0.170 |  |
| 2026-08-02 00:05:41 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | -0.251 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)