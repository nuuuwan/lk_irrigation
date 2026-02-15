# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--15_17:16:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **73,900 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 17:16:52 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:13:15 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:12:07 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:11:00 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:10:43 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-02-15 17:08:36 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:08:11 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.058 |  |
| 2026-02-15 17:08:04 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.027 |  |
| 2026-02-15 17:07:02 | Glencourse (Kelani Ganga) | 8.29 | 🟢 Normal | -0.010 |  |
| 2026-02-15 17:06:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.009 |  |
| 2026-02-15 17:05:37 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-02-15 17:05:33 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:05:22 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:05:17 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.012 |  |
| 2026-02-15 17:04:47 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:04:43 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:04:41 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.029 |  |
| 2026-02-15 17:04:33 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:04:25 | Weraganthota (Mahaweli Ganga) | -2.41 | 🟢 Normal | -0.104 |  |
| 2026-02-15 17:04:21 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:04:13 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-02-15 17:04:10 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:04:07 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:03:29 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.057 |  |
| 2026-02-15 17:03:13 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-02-15 17:03:11 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.068 |  |
| 2026-02-15 17:03:11 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.043 |  |
| 2026-02-15 17:03:07 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-15 17:02:58 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:02:23 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:02:17 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:02:02 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:01:50 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:01:46 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-02-15 17:01:46 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:01:09 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-02-15 17:01:09 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | -0.020 |  |
| 2026-02-15 17:00:50 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:00:45 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:00:28 | Manampitiya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.152 |  |
| 2026-02-15 17:00:02 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-02-15 16:39:01 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 17:03:07 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-15 17:01:50 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:04:47 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:00:50 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:02:02 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:02:58 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:12:07 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:04:07 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:02:17 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:13:15 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:11:00 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:04:43 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:00:45 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:02:23 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:05:33 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:05:22 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:16:52 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:04:10 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:08:36 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:04:21 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:10:43 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-02-15 17:06:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.009 |  |
| 2026-02-15 17:07:02 | Glencourse (Kelani Ganga) | 8.29 | 🟢 Normal | -0.010 |  |
| 2026-02-15 17:04:13 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-02-15 17:01:09 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-02-15 17:00:02 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-02-15 17:03:13 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-02-15 17:01:46 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-02-15 17:05:17 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.012 |  |
| 2026-02-15 17:01:09 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | -0.020 |  |
| 2026-02-15 17:05:37 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-02-15 17:08:04 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.027 |  |
| 2026-02-15 17:04:41 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.029 |  |
| 2026-02-15 17:03:11 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.043 |  |
| 2026-02-15 17:03:29 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.057 |  |
| 2026-02-15 17:08:11 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.058 |  |
| 2026-02-15 17:03:11 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.068 |  |
| 2026-02-15 17:04:25 | Weraganthota (Mahaweli Ganga) | -2.41 | 🟢 Normal | -0.104 |  |
| 2026-02-15 17:00:28 | Manampitiya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.152 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)