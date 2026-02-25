# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--25_12:09:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **82,662 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 12:09:14 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:08:24 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | -0.009 |  |
| 2026-02-25 12:07:31 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:06:22 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-02-25 12:05:44 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-25 12:05:15 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | -0.020 |  |
| 2026-02-25 12:05:04 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:04:55 | Putupaula (Kalu Ganga) | 0.24 | 🟢 Normal | -0.069 |  |
| 2026-02-25 12:04:51 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:04:49 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | -0.035 |  |
| 2026-02-25 12:04:48 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:04:44 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:04:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-25 12:04:34 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:04:22 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:04:18 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:03:42 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-02-25 12:03:15 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.030 |  |
| 2026-02-25 12:03:14 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:02:49 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:02:48 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-02-25 12:02:45 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.030 |  |
| 2026-02-25 12:02:42 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:02:40 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:02:35 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:02:33 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:02:23 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-02-25 12:02:22 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:02:06 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:02:06 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 12:02:05 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-25 12:01:58 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:01:34 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.012 |  |
| 2026-02-25 12:01:33 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:01:31 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | -3.877 |  |
| 2026-02-25 12:01:29 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-02-25 12:01:17 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:01:13 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | -0.011 |  |
| 2026-02-25 12:00:20 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.033 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 12:02:23 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-02-25 12:04:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-25 12:05:44 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-25 12:02:05 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-25 12:02:06 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 12:01:17 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:02:06 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:04:51 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:01:33 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:04:48 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:05:04 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:09:14 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:02:49 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:03:14 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:01:58 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:04:11 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:02:35 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:02:42 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:02:22 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:04:22 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:04:44 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:04:34 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:07:31 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:04:18 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:02:33 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-25 12:08:24 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | -0.009 |  |
| 2026-02-25 12:02:48 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-02-25 12:06:22 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-02-25 12:01:29 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-02-25 12:01:13 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | -0.011 |  |
| 2026-02-25 12:01:34 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.012 |  |
| 2026-02-25 12:03:42 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-02-25 12:05:15 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | -0.020 |  |
| 2026-02-25 12:02:45 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.030 |  |
| 2026-02-25 12:03:15 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.030 |  |
| 2026-02-25 12:00:20 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.033 |  |
| 2026-02-25 12:04:49 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | -0.035 |  |
| 2026-02-25 12:04:55 | Putupaula (Kalu Ganga) | 0.24 | 🟢 Normal | -0.069 |  |
| 2026-02-25 12:01:31 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | -3.877 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)