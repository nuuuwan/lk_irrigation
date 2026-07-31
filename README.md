# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--31_06:20:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **220,928 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-31 06:20:35 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:19:22 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-07-31 06:13:45 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:09:55 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 06:08:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.037 |  |
| 2026-07-31 06:07:55 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:07:42 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:07:17 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-31 06:06:35 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | -0.049 |  |
| 2026-07-31 06:05:48 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:05:47 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-31 06:04:52 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:04:30 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | -0.085 |  |
| 2026-07-31 06:04:24 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.328 | 🔺 Rising |
| 2026-07-31 06:04:18 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-31 06:04:12 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-07-31 06:04:00 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:03:55 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:03:51 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:03:23 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:03:21 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-31 06:03:10 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-31 06:03:06 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:02:35 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:02:24 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:02:20 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-07-31 06:01:58 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:01:37 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-07-31 06:01:30 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:01:19 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:01:14 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.032 |  |
| 2026-07-31 06:01:09 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:00:46 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:00:34 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-07-31 06:00:33 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.096 |  |
| 2026-07-31 06:00:18 | Weraganthota (Mahaweli Ganga) | -3.43 | 🟢 Normal | -0.009 |  |
| 2026-07-31 05:37:25 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-31 06:04:24 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.328 | 🔺 Rising |
| 2026-07-31 06:01:37 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-07-31 06:02:20 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-07-31 06:04:12 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-07-31 06:19:22 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-07-31 06:04:18 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-31 06:05:47 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-31 06:03:10 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-31 06:03:21 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-31 06:09:55 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 06:07:17 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-31 06:02:35 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:00:46 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:02:24 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:03:51 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:01:19 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:20:35 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:04:12 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:01:30 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:04:00 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:01:09 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:04:52 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:07:42 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:03:06 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:03:23 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:01:58 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:07:55 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:03:55 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:13:45 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-31 03:05:59 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:05:48 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-31 06:00:18 | Weraganthota (Mahaweli Ganga) | -3.43 | 🟢 Normal | -0.009 |  |
| 2026-07-30 18:01:03 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-07-31 06:00:34 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-07-31 06:01:14 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.032 |  |
| 2026-07-31 06:08:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.037 |  |
| 2026-07-31 06:06:35 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | -0.049 |  |
| 2026-07-31 06:04:30 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | -0.085 |  |
| 2026-07-31 06:00:33 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)