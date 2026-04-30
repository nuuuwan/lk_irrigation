# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_14:03:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **139,137 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 14:03:47 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.011 |  |
| 2026-04-30 14:03:47 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-30 14:03:14 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-04-30 14:03:13 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-04-30 14:03:00 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-30 14:02:47 | Horowpothana (Yan Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-04-30 14:02:42 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | -0.020 |  |
| 2026-04-30 14:02:27 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.032 |  |
| 2026-04-30 14:02:25 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-30 14:02:22 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-04-30 14:01:51 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-30 14:01:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.09 | 🟢 Normal | -0.005 |  |
| 2026-04-30 14:01:39 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.090 |  |
| 2026-04-30 14:01:32 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-30 14:01:23 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 14:01:17 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-30 14:01:17 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-30 14:01:11 | Thanthirimale (Malwathu Oya) | 2.95 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-30 14:01:09 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 14:00:10 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-30 14:00:10 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-30 14:00:10 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.042 |  |
| 2026-04-30 14:00:09 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-30 13:35:19 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-30 13:22:10 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-30 13:11:24 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 14:00:09 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-30 13:22:10 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-30 14:01:17 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-30 14:01:32 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-30 14:01:11 | Thanthirimale (Malwathu Oya) | 2.95 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-30 14:02:25 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-30 13:35:19 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-30 13:03:08 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 14:01:09 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 14:01:23 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 13:04:14 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 14:03:00 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-30 13:10:27 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-30 14:02:47 | Horowpothana (Yan Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-04-30 13:01:58 | Galgamuwa (Mee Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-30 14:01:51 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-30 13:03:24 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-30 13:11:24 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-30 14:01:17 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-30 14:00:10 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-30 14:03:47 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-30 13:04:40 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 14:03:14 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-04-30 13:09:30 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-30 14:00:10 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-30 14:01:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.09 | 🟢 Normal | -0.005 |  |
| 2026-04-30 13:07:49 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-04-30 13:04:12 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-04-30 14:02:22 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-04-30 13:04:05 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-30 14:03:47 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.011 |  |
| 2026-04-30 13:07:15 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.019 |  |
| 2026-04-30 13:06:53 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.019 |  |
| 2026-04-30 13:06:56 | Ellagawa (Kalu Ganga) | 4.47 | 🟢 Normal | -0.019 |  |
| 2026-04-30 13:05:09 | Dunamale (Aththanagalu Oya) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-04-30 14:02:42 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | -0.020 |  |
| 2026-04-30 14:02:27 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.032 |  |
| 2026-04-30 14:00:10 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.042 |  |
| 2026-04-30 14:01:39 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)