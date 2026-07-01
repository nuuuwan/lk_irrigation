# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--01_10:11:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **194,254 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 10:11:21 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | -0.025 |  |
| 2026-07-01 10:10:52 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.009 |  |
| 2026-07-01 10:10:09 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:09:41 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.048 |  |
| 2026-07-01 10:09:01 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-07-01 10:08:57 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:08:41 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.120 |  |
| 2026-07-01 10:07:36 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.009 |  |
| 2026-07-01 10:07:35 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.023 |  |
| 2026-07-01 10:07:01 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-01 10:06:45 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-07-01 10:06:15 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:05:47 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.013 |  |
| 2026-07-01 10:05:19 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-07-01 10:04:13 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:04:05 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.030 |  |
| 2026-07-01 10:03:40 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:03:22 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.059 |  |
| 2026-07-01 10:03:17 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-07-01 10:03:10 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | -0.051 |  |
| 2026-07-01 10:02:59 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:02:58 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:02:25 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:02:19 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-07-01 10:02:15 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | -0.101 |  |
| 2026-07-01 10:01:54 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:01:48 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-07-01 10:01:35 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:01:33 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:01:25 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.030 |  |
| 2026-07-01 10:01:19 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:01:15 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | -0.011 |  |
| 2026-07-01 10:01:08 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:01:05 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-07-01 10:01:04 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:00:40 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:00:22 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:00:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.36 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 10:01:05 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-07-01 10:07:01 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-01 10:00:22 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:04:13 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:02:59 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:01:19 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:01:54 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:00:40 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:08:57 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:01:33 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:02:25 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:01:08 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:03:40 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:06:15 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:10:09 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:01:04 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:00:33 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:02:58 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:01:35 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:07:36 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.009 |  |
| 2026-07-01 10:10:52 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.009 |  |
| 2026-07-01 10:09:01 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-07-01 10:06:45 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-07-01 10:02:19 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-07-01 10:01:48 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-07-01 10:03:17 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-07-01 10:05:19 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-07-01 10:01:15 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | -0.011 |  |
| 2026-07-01 10:05:47 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.013 |  |
| 2026-07-01 10:00:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.36 | 🟢 Normal | -0.022 |  |
| 2026-07-01 10:07:35 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.023 |  |
| 2026-07-01 10:11:21 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | -0.025 |  |
| 2026-07-01 10:04:05 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.030 |  |
| 2026-07-01 10:01:25 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.030 |  |
| 2026-07-01 10:09:41 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.048 |  |
| 2026-07-01 10:03:10 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | -0.051 |  |
| 2026-07-01 10:03:22 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.059 |  |
| 2026-07-01 10:02:15 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | -0.101 |  |
| 2026-07-01 10:08:41 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)