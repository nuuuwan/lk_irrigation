# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--20_21:25:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **78,495 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 21:25:08 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-02-20 21:23:12 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-20 21:22:42 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-20 21:10:10 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.095 |  |
| 2026-02-20 21:09:31 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-20 21:08:26 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-02-20 21:07:51 | Padiyathalawa (Maduru Oya) | 1.98 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-20 21:07:25 | Glencourse (Kelani Ganga) | 8.29 | 🟢 Normal | -0.041 |  |
| 2026-02-20 21:07:01 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.028 |  |
| 2026-02-20 21:06:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.63 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-02-20 21:05:58 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-02-20 21:05:12 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-02-20 21:05:10 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-02-20 21:04:58 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.049 |  |
| 2026-02-20 21:04:46 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-20 21:04:27 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 21:04:11 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-02-20 21:04:06 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-20 21:04:05 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-02-20 21:03:57 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-20 21:03:43 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.029 |  |
| 2026-02-20 21:03:39 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-20 21:02:52 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-20 21:02:46 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.011 |  |
| 2026-02-20 21:02:29 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-20 21:02:29 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-20 21:02:27 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-20 21:02:24 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-20 21:02:23 | Manampitiya (Mahaweli Ganga) | 3.10 | 🟡 Alert | 0.000 |  |
| 2026-02-20 21:02:14 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-20 21:02:03 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-20 21:01:46 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-02-20 21:01:45 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-02-20 21:01:36 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-20 21:01:27 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-20 21:01:11 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 21:02:23 | Manampitiya (Mahaweli Ganga) | 3.10 | 🟡 Alert | 0.000 |  |
| 2026-02-20 21:06:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.63 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-02-20 21:01:46 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-02-20 21:05:10 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-02-20 21:25:08 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-02-20 21:04:11 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-02-20 21:07:51 | Padiyathalawa (Maduru Oya) | 1.98 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-20 21:02:24 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-20 21:03:57 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-20 21:04:46 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-20 21:02:29 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-20 21:04:06 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-20 21:01:11 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-20 21:01:27 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-20 21:23:12 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-20 18:04:38 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-20 20:02:19 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-20 21:03:39 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-20 21:05:58 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-02-20 21:02:03 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-20 21:02:29 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-20 21:04:27 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 21:02:14 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-20 21:22:42 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-20 18:01:33 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-20 21:01:36 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-20 21:02:52 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-20 21:04:05 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-02-20 20:00:55 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-02-20 21:02:46 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.011 |  |
| 2026-02-20 21:05:12 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-02-20 21:01:45 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-02-20 21:07:01 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.028 |  |
| 2026-02-20 21:03:43 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.029 |  |
| 2026-02-20 21:08:26 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-02-20 21:07:25 | Glencourse (Kelani Ganga) | 8.29 | 🟢 Normal | -0.041 |  |
| 2026-02-20 21:04:58 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.049 |  |
| 2026-02-20 18:02:20 | Weraganthota (Mahaweli Ganga) | -1.32 | 🟢 Normal | -0.051 |  |
| 2026-02-20 21:10:10 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)