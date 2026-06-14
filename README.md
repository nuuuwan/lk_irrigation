# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--14_18:02:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **179,337 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 18:02:32 | Giriulla (Maha Oya) | 1.69 | 🟢 Normal | -0.030 |  |
| 2026-06-14 18:02:24 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-14 18:02:22 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.041 |  |
| 2026-06-14 18:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.11 | 🟡 Alert | -0.031 |  |
| 2026-06-14 18:02:17 | Magura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.073 |  |
| 2026-06-14 18:01:56 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-14 18:01:52 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-14 18:01:52 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-06-14 18:01:48 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-14 18:01:41 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-06-14 18:01:31 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-14 18:00:58 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-14 18:00:54 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-14 18:00:38 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-06-14 18:00:21 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-14 18:00:17 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-06-14 18:00:12 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-14 17:59:31 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.006 |  |
| 2026-06-14 17:14:58 | Rathnapura (Kalu Ganga) | 2.97 | 🟢 Normal | -0.034 |  |
| 2026-06-14 17:13:26 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-06-14 17:12:46 | Magura (Kalu Ganga) | 2.56 | 🟢 Normal | -0.073 |  |
| 2026-06-14 17:11:36 | Baddegama (Gin Ganga) | 2.60 | 🟢 Normal | -0.026 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 18:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.11 | 🟡 Alert | -0.031 |  |
| 2026-06-14 17:02:54 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-06-14 18:01:48 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-14 18:02:24 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-14 18:01:52 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-14 17:00:16 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-14 18:00:12 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-14 18:01:56 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-14 18:00:54 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-14 14:02:49 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-14 18:00:58 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-14 17:00:31 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-14 18:00:17 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-06-14 18:01:52 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-06-14 17:01:33 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-06-14 18:00:21 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-14 18:01:31 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-14 17:03:10 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-14 17:59:31 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.006 |  |
| 2026-06-14 17:10:31 | Moragaswewa (Deduru Oya) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-06-14 17:05:36 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | -0.009 |  |
| 2026-06-14 18:01:41 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-06-14 17:13:26 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-06-14 17:03:59 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-06-14 18:00:38 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-06-14 17:02:26 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-06-14 17:01:39 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.011 |  |
| 2026-06-14 17:06:54 | Badalgama (Maha Oya) | 3.01 | 🟢 Normal | -0.020 |  |
| 2026-06-14 17:04:21 | Galgamuwa (Mee Oya) | 0.65 | 🟢 Normal | -0.021 |  |
| 2026-06-14 17:11:36 | Baddegama (Gin Ganga) | 2.60 | 🟢 Normal | -0.026 |  |
| 2026-06-14 18:02:32 | Giriulla (Maha Oya) | 1.69 | 🟢 Normal | -0.030 |  |
| 2026-06-14 17:06:26 | Panadugama (Nilwala Ganga) | 3.64 | 🟢 Normal | -0.031 |  |
| 2026-06-14 17:14:58 | Rathnapura (Kalu Ganga) | 2.97 | 🟢 Normal | -0.034 |  |
| 2026-06-14 17:09:17 | Dunamale (Aththanagalu Oya) | 2.94 | 🟢 Normal | -0.035 |  |
| 2026-06-14 18:02:22 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.041 |  |
| 2026-06-14 17:03:18 | Hanwella (Kelani Ganga) | 3.27 | 🟢 Normal | -0.050 |  |
| 2026-06-14 18:02:17 | Magura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.073 |  |
| 2026-06-14 17:01:13 | Ellagawa (Kalu Ganga) | 8.02 | 🟢 Normal | -0.083 |  |
| 2026-06-14 17:03:01 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)