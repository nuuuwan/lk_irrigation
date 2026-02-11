# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--11_10:13:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **70,047 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-11 10:13:59 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.037 |  |
| 2026-02-11 10:11:51 | Peradeniya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-02-11 10:11:44 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:10:16 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:09:47 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-02-11 10:08:13 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | -0.009 |  |
| 2026-02-11 10:07:52 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:06:36 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:06:14 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-02-11 10:05:42 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:05:20 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:05:13 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.105 |  |
| 2026-02-11 10:04:35 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.029 |  |
| 2026-02-11 10:04:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.029 |  |
| 2026-02-11 10:03:53 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-11 10:03:50 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-11 10:03:31 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:03:29 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.012 |  |
| 2026-02-11 10:03:26 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:03:05 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:03:04 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:02:48 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.111 |  |
| 2026-02-11 10:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:02:36 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:02:29 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-11 10:02:11 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:01:57 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:01:46 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:01:42 | Dunamale (Aththanagalu Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:01:41 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | -0.012 |  |
| 2026-02-11 10:01:30 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.063 |  |
| 2026-02-11 10:01:29 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:01:09 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:00:48 | Weraganthota (Mahaweli Ganga) | -2.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-11 10:00:44 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-02-11 10:00:39 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-02-11 10:00:34 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-02-11 09:58:38 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-11 10:00:44 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-02-11 10:11:51 | Peradeniya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-02-11 10:02:29 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-11 10:03:53 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-11 10:03:50 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-11 10:00:48 | Weraganthota (Mahaweli Ganga) | -2.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-11 10:01:29 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:03:04 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:03:26 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:01:46 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:06:36 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:01:09 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:07:52 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:10:16 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:02:36 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:03:31 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:01:57 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:01:42 | Dunamale (Aththanagalu Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:02:11 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:05:20 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:05:42 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:11:44 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:03:05 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-11 10:08:13 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | -0.009 |  |
| 2026-02-11 10:09:47 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-02-11 10:00:34 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-02-11 10:00:39 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-02-11 10:01:41 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | -0.012 |  |
| 2026-02-11 10:03:29 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.012 |  |
| 2026-02-11 09:06:51 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.022 |  |
| 2026-02-11 09:58:38 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.022 |  |
| 2026-02-11 10:04:35 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.029 |  |
| 2026-02-11 10:04:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.029 |  |
| 2026-02-11 10:06:14 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-02-11 10:13:59 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.037 |  |
| 2026-02-11 10:01:30 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.063 |  |
| 2026-02-11 10:05:13 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.105 |  |
| 2026-02-11 10:02:48 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)