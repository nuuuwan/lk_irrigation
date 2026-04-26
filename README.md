# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_12:18:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **135,536 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 12:18:24 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.016 |  |
| 2026-04-26 12:17:10 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:09:34 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:08:53 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.046 |  |
| 2026-04-26 12:08:18 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-26 12:07:53 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:07:53 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.009 |  |
| 2026-04-26 12:07:52 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.024 |  |
| 2026-04-26 12:06:30 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-04-26 12:06:13 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-26 12:05:44 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:05:37 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | -0.010 |  |
| 2026-04-26 12:05:27 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:05:11 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.019 |  |
| 2026-04-26 12:04:47 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:04:45 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-26 12:03:53 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:03:41 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:03:38 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:03:19 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:03:13 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-04-26 12:03:11 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:03:04 | Katharagama (Menik Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:02:59 | Urawa (Nilwala Ganga) | 2.00 | 🟢 Normal | -9.278 |  |
| 2026-04-26 12:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.040 |  |
| 2026-04-26 12:02:47 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:02:45 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.034 |  |
| 2026-04-26 12:02:26 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:02:19 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.030 |  |
| 2026-04-26 12:02:14 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.029 |  |
| 2026-04-26 12:02:11 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-26 12:02:02 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.020 |  |
| 2026-04-26 12:01:45 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:01:35 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:01:19 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:01:18 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.031 |  |
| 2026-04-26 12:01:15 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:00:44 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.021 |  |
| 2026-04-26 12:00:40 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-04-26 11:56:31 | Urawa (Nilwala Ganga) | 3.00 | 🟡 Alert | -9.278 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 12:02:11 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-26 12:08:18 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-26 12:04:45 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-26 12:01:15 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:01:45 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:03:19 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:01:19 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:07:53 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:03:11 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:17:10 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:09:34 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:03:41 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:03:53 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:00:40 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:05:27 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:01:35 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:05:44 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:03:04 | Katharagama (Menik Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:04:47 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:02:26 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:03:38 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:07:53 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.009 |  |
| 2026-04-26 12:05:37 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | -0.010 |  |
| 2026-04-26 12:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-04-26 12:06:13 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-26 12:06:30 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-04-26 12:18:24 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.016 |  |
| 2026-04-26 12:05:11 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.019 |  |
| 2026-04-26 12:02:02 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.020 |  |
| 2026-04-26 12:03:13 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-04-26 12:00:44 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.021 |  |
| 2026-04-26 12:07:52 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.024 |  |
| 2026-04-26 12:02:14 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.029 |  |
| 2026-04-26 12:02:19 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.030 |  |
| 2026-04-26 12:01:18 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.031 |  |
| 2026-04-26 12:02:45 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.034 |  |
| 2026-04-26 12:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.040 |  |
| 2026-04-26 12:08:53 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.046 |  |
| 2026-04-26 12:02:59 | Urawa (Nilwala Ganga) | 2.00 | 🟢 Normal | -9.278 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)