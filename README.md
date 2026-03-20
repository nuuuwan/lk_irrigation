# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--20_17:26:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **102,673 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 17:26:36 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-20 17:26:23 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.022 |  |
| 2026-03-20 17:13:50 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-03-20 17:10:46 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.028 |  |
| 2026-03-20 17:09:43 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.053 |  |
| 2026-03-20 17:09:20 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-03-20 17:08:47 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.009 |  |
| 2026-03-20 17:08:45 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-20 17:07:30 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-20 17:07:24 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-03-20 17:06:46 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-03-20 17:05:45 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-20 17:05:33 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-03-20 17:05:30 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 17:05:14 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.048 |  |
| 2026-03-20 17:03:50 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-03-20 17:03:48 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-03-20 17:03:48 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-03-20 17:03:13 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-20 17:03:08 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-20 17:03:03 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-20 17:03:00 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 17:02:59 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 17:02:36 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-03-20 17:02:34 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-20 17:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-03-20 17:02:33 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-20 17:02:22 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-20 17:02:21 | Kithulgala (Kelani Ganga) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 17:02:15 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-03-20 17:02:07 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-03-20 17:02:06 | Weraganthota (Mahaweli Ganga) | -2.79 | 🟢 Normal | -0.109 |  |
| 2026-03-20 17:01:52 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 17:01:28 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | -0.031 |  |
| 2026-03-20 17:01:15 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.041 |  |
| 2026-03-20 17:01:05 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-20 17:01:02 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-20 17:00:33 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.161 |  |
| 2026-03-20 17:00:11 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 17:13:50 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-03-20 17:02:34 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-20 17:02:21 | Kithulgala (Kelani Ganga) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 17:01:52 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 17:00:11 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-20 17:01:05 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-20 17:07:30 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-20 17:26:36 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-20 17:01:02 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-20 17:03:00 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 17:03:03 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-20 17:03:13 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-20 17:02:33 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-20 17:03:08 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-20 17:05:30 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 17:02:59 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 17:09:20 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-03-20 17:08:45 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-20 17:05:45 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-20 17:08:47 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.009 |  |
| 2026-03-20 17:05:33 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-03-20 17:03:50 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-03-20 17:03:48 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-03-20 17:03:48 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-03-20 17:02:22 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-20 17:02:15 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-03-20 17:02:07 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-03-20 17:07:24 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-03-20 17:02:36 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-03-20 17:06:46 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-03-20 17:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-03-20 17:26:23 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.022 |  |
| 2026-03-20 17:10:46 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.028 |  |
| 2026-03-20 17:01:28 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | -0.031 |  |
| 2026-03-20 17:01:15 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.041 |  |
| 2026-03-20 17:05:14 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.048 |  |
| 2026-03-20 17:09:43 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.053 |  |
| 2026-03-20 17:02:06 | Weraganthota (Mahaweli Ganga) | -2.79 | 🟢 Normal | -0.109 |  |
| 2026-03-20 17:00:33 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.161 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)