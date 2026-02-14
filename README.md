# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--14_11:14:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **72,782 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 11:14:30 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.005 |  |
| 2026-02-14 11:12:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.77 | 🟢 Normal | -0.029 |  |
| 2026-02-14 11:12:19 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-14 11:11:17 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.027 |  |
| 2026-02-14 11:09:58 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-14 11:07:16 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 11:06:53 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-14 11:06:28 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-02-14 11:06:23 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.029 |  |
| 2026-02-14 11:06:22 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-14 11:06:05 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-02-14 11:05:50 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-14 11:05:10 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-14 11:04:54 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.020 |  |
| 2026-02-14 11:04:37 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 11:04:32 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2026-02-14 11:04:20 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-14 11:03:54 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-02-14 11:03:49 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-14 11:03:33 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-14 11:03:29 | Manampitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | 11.688 | 🔺 Rising |
| 2026-02-14 11:03:29 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-14 11:03:01 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-14 11:02:48 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-14 11:02:47 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-14 11:02:46 | Weraganthota (Mahaweli Ganga) | -2.37 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-02-14 11:02:35 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-14 11:02:21 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.013 |  |
| 2026-02-14 11:02:09 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-02-14 11:01:50 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-14 11:01:39 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.104 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 11:03:29 | Manampitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | 11.688 | 🔺 Rising |
| 2026-02-14 11:02:46 | Weraganthota (Mahaweli Ganga) | -2.37 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-02-14 11:06:28 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-02-14 11:01:39 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-02-14 11:12:19 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-14 11:06:05 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-02-14 11:06:53 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-14 11:01:50 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-14 11:04:37 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 11:01:31 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 11:05:50 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-14 11:02:35 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-14 11:00:23 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-14 11:04:20 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-14 11:02:48 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-14 11:02:47 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-14 11:06:22 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-14 11:09:58 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-14 11:03:33 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:03:54 | Dunamale (Aththanagalu Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-14 11:07:16 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 11:03:49 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-14 11:00:44 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-02-14 11:03:01 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-14 11:05:10 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-14 11:14:30 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.005 |  |
| 2026-02-14 11:03:54 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-02-14 11:02:09 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-02-14 11:01:07 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-02-14 11:03:29 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-14 11:01:09 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-02-14 11:01:14 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | -0.011 |  |
| 2026-02-14 11:00:47 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-02-14 11:02:21 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.013 |  |
| 2026-02-14 11:04:32 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2026-02-14 11:04:54 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.020 |  |
| 2026-02-14 11:11:17 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.027 |  |
| 2026-02-14 11:06:23 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.029 |  |
| 2026-02-14 11:12:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.77 | 🟢 Normal | -0.029 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)