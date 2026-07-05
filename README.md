# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_09:41:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **197,798 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **3** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 09:41:18 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-05 09:18:25 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | -0.031 |  |
| 2026-07-05 09:17:59 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 09:01:00 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-07-05 09:06:51 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-05 09:02:41 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-05 09:07:00 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-05 09:03:12 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-05 09:02:26 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-07-05 09:00:38 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 09:00:39 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 09:02:49 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-05 09:00:37 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 09:04:14 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-05 09:03:25 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 09:04:55 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-05 09:05:19 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-05 09:17:59 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-07-05 09:05:22 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-05 09:41:18 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-05 09:06:24 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-05 09:01:15 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-05 09:00:14 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-05 09:08:09 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-05 09:04:09 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-05 09:02:28 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 09:05:43 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-07-05 09:08:23 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.011 |  |
| 2026-07-05 09:08:31 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | -0.018 |  |
| 2026-07-05 09:08:02 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.020 |  |
| 2026-07-05 09:02:58 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.021 |  |
| 2026-07-05 09:03:52 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-07-05 09:01:26 | Ellagawa (Kalu Ganga) | 5.74 | 🟢 Normal | -0.030 |  |
| 2026-07-05 09:04:06 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.031 |  |
| 2026-07-05 09:18:25 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | -0.031 |  |
| 2026-07-05 09:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.37 | 🟢 Normal | -0.033 |  |
| 2026-07-05 09:01:31 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.042 |  |
| 2026-07-05 09:00:30 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.042 |  |
| 2026-07-05 09:05:48 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.049 |  |
| 2026-07-05 09:03:00 | Giriulla (Maha Oya) | 1.92 | 🟢 Normal | -0.049 |  |
| 2026-07-05 09:03:22 | Hanwella (Kelani Ganga) | 3.22 | 🟢 Normal | -0.050 |  |
| 2026-07-05 09:05:32 | Glencourse (Kelani Ganga) | 11.12 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)