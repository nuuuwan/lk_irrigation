# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--01_17:09:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **194,528 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 17:09:51 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:09:51 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -0.015 |  |
| 2026-07-01 17:08:00 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-07-01 17:07:38 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-07-01 17:06:40 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:06:19 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-07-01 17:06:02 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:05:59 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-07-01 17:05:26 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:05:25 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:03:56 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:03:51 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:03:42 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:03:30 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | -0.010 |  |
| 2026-07-01 17:03:28 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:03:27 | Hanwella (Kelani Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-07-01 17:03:23 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 17:03:18 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.034 |  |
| 2026-07-01 17:03:13 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:03:04 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.022 |  |
| 2026-07-01 17:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.00 | 🟢 Normal | -0.053 |  |
| 2026-07-01 17:02:29 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:02:13 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | -0.045 |  |
| 2026-07-01 17:02:12 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.050 |  |
| 2026-07-01 17:02:03 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.062 |  |
| 2026-07-01 17:01:55 | Rathnapura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.024 |  |
| 2026-07-01 17:01:45 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:01:33 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:01:26 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.021 |  |
| 2026-07-01 17:01:21 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:01:17 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-07-01 17:01:15 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:01:15 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.033 |  |
| 2026-07-01 17:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-07-01 17:01:11 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2026-07-01 17:00:56 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:00:43 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:00:18 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:58:14 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 17:01:11 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2026-07-01 17:06:19 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-07-01 17:03:23 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 17:03:42 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:02:29 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:03:51 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:01:21 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:00:56 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:01:33 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:05:26 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:00:18 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:05:25 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:03:28 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:00:43 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:06:40 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:03:56 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:01:15 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:01:45 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:09:51 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:03:13 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:06:02 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:05:26 | Panadugama (Nilwala Ganga) | 2.83 | 🟢 Normal | -0.005 |  |
| 2026-07-01 17:08:00 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-07-01 17:05:59 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-07-01 17:07:38 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-07-01 17:03:30 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | -0.010 |  |
| 2026-07-01 17:03:27 | Hanwella (Kelani Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-07-01 17:01:17 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-07-01 17:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-07-01 17:09:51 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -0.015 |  |
| 2026-07-01 17:01:26 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.021 |  |
| 2026-07-01 17:03:04 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.022 |  |
| 2026-07-01 17:01:55 | Rathnapura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.024 |  |
| 2026-07-01 17:01:15 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.033 |  |
| 2026-07-01 17:03:18 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.034 |  |
| 2026-07-01 17:02:13 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | -0.045 |  |
| 2026-07-01 17:02:12 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.050 |  |
| 2026-07-01 17:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.00 | 🟢 Normal | -0.053 |  |
| 2026-07-01 17:02:03 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)