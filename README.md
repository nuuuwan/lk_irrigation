# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--07_09:11:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **66,454 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 09:11:25 | Padiyathalawa (Maduru Oya) | 1.34 | 🟢 Normal | -0.052 |  |
| 2026-02-07 09:10:10 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.009 |  |
| 2026-02-07 09:10:10 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-02-07 09:09:26 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-07 09:09:16 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.072 |  |
| 2026-02-07 09:06:37 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.116 |  |
| 2026-02-07 09:06:33 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-02-07 09:06:14 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.159 |  |
| 2026-02-07 09:05:34 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-07 09:04:50 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-02-07 09:04:22 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-07 09:04:21 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 09:04:11 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-07 09:04:00 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.162 |  |
| 2026-02-07 09:03:03 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-07 09:03:03 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 09:02:54 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-07 09:02:46 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-07 09:02:37 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-02-07 09:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 09:02:28 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -216.000 |  |
| 2026-02-07 09:02:28 | Weraganthota (Mahaweli Ganga) | -1.77 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-02-07 09:02:27 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -216.000 |  |
| 2026-02-07 09:02:24 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 09:02:16 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 09:02:05 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.492 |  |
| 2026-02-07 09:01:54 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-02-07 09:01:53 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | -0.011 |  |
| 2026-02-07 09:01:43 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-07 09:01:42 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-02-07 09:01:32 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-07 09:01:32 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-02-07 09:01:24 | Horowpothana (Yan Oya) | 2.69 | 🟢 Normal | -0.031 |  |
| 2026-02-07 09:01:22 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-07 09:01:08 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-02-07 09:01:03 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-07 09:00:51 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 09:00:41 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-02-07 09:00:27 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 09:02:28 | Weraganthota (Mahaweli Ganga) | -1.77 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-02-07 09:01:42 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-02-07 09:02:24 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 09:04:22 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-07 09:00:27 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 09:00:51 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 09:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 09:04:21 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 09:03:03 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 09:01:43 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-07 09:01:32 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-07 09:02:54 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-07 09:01:22 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-07 09:02:46 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-07 09:04:11 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-07 09:10:10 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-02-07 09:06:33 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-02-07 09:02:16 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 09:05:34 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-07 09:09:26 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-07 09:03:03 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-07 09:01:03 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-07 09:10:10 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.009 |  |
| 2026-02-07 09:01:54 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-02-07 09:02:37 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-02-07 09:01:32 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-02-07 09:01:08 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-02-07 09:00:41 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-02-07 09:04:50 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-02-07 09:01:53 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | -0.011 |  |
| 2026-02-07 09:01:24 | Horowpothana (Yan Oya) | 2.69 | 🟢 Normal | -0.031 |  |
| 2026-02-07 08:05:51 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.040 |  |
| 2026-02-07 09:11:25 | Padiyathalawa (Maduru Oya) | 1.34 | 🟢 Normal | -0.052 |  |
| 2026-02-07 09:09:16 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.072 |  |
| 2026-02-07 09:06:37 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.116 |  |
| 2026-02-07 09:06:14 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.159 |  |
| 2026-02-07 09:04:00 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.162 |  |
| 2026-02-07 09:02:05 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.492 |  |
| 2026-02-07 09:02:28 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -216.000 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)