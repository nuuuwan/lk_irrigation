# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--11_14:18:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **203,401 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **8** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 14:18:36 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-11 14:16:53 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 14:16:28 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-07-11 14:15:03 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-07-11 14:14:56 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-11 14:11:42 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-11 14:11:00 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-11 14:10:28 | Glencourse (Kelani Ganga) | 9.73 | 🟢 Normal | 0.044 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 14:01:31 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.319 | 🔺 Rising |
| 2026-07-11 14:03:02 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-07-11 14:10:28 | Glencourse (Kelani Ganga) | 9.73 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-07-11 14:16:28 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-07-11 14:11:42 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-11 14:01:06 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-11 14:11:00 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-11 14:02:27 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-11 14:02:17 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-11 14:02:34 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-11 14:07:06 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-11 14:02:21 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:04:32 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-07-11 14:01:11 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 14:14:56 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-11 14:00:09 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-11 14:01:21 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 14:03:50 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-11 14:05:10 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-07-11 14:04:21 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-11 14:01:18 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-11 14:16:53 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 14:18:36 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-11 14:09:42 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-11 14:09:07 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.009 |  |
| 2026-07-11 14:05:41 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-07-11 14:15:03 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-07-11 14:02:04 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-07-11 14:02:14 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-07-11 14:02:06 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-07-11 14:03:31 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.011 |  |
| 2026-07-11 14:08:20 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.019 |  |
| 2026-07-11 14:00:42 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | -0.020 |  |
| 2026-07-11 14:02:02 | Ellagawa (Kalu Ganga) | 4.64 | 🟢 Normal | -0.020 |  |
| 2026-07-11 14:03:06 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.030 |  |
| 2026-07-11 14:03:46 | Hanwella (Kelani Ganga) | 1.41 | 🟢 Normal | -0.030 |  |
| 2026-07-11 14:00:09 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.032 |  |
| 2026-07-11 14:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.053 |  |
| 2026-07-11 14:04:44 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)