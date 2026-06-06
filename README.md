# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_06:32:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **171,757 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 06:32:51 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | -0.001 |  |
| 2026-06-06 06:22:42 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.009 |  |
| 2026-06-06 06:22:41 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | -0.068 |  |
| 2026-06-06 06:13:17 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-06 06:10:32 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-06 06:07:56 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.074 |  |
| 2026-06-06 06:07:31 | Rathnapura (Kalu Ganga) | 3.30 | 🟢 Normal | -0.059 |  |
| 2026-06-06 06:07:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.11 | 🟢 Normal | -0.161 |  |
| 2026-06-06 06:05:53 | Baddegama (Gin Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-06-06 06:05:37 | Glencourse (Kelani Ganga) | 11.80 | 🟢 Normal | -0.104 |  |
| 2026-06-06 06:05:33 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-06 06:05:28 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.009 |  |
| 2026-06-06 06:05:25 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-06 06:04:42 | Dunamale (Aththanagalu Oya) | 3.33 | 🟡 Alert | 0.000 |  |
| 2026-06-06 06:04:34 | Hanwella (Kelani Ganga) | 3.70 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-06 06:03:53 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-06 06:03:32 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-06-06 06:03:19 | Deraniyagala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.030 |  |
| 2026-06-06 06:03:15 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.061 |  |
| 2026-06-06 06:03:12 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-06 06:02:51 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.030 |  |
| 2026-06-06 06:02:50 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-06 06:02:33 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 06:02:29 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.010 |  |
| 2026-06-06 06:02:29 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 06:02:25 | Ellagawa (Kalu Ganga) | 7.24 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-06 06:02:07 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-06-06 06:02:02 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.115 |  |
| 2026-06-06 06:01:56 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-06-06 06:01:23 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-06 06:01:21 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | -0.046 |  |
| 2026-06-06 06:01:10 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-06 06:01:05 | Nawalapitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-06 06:00:58 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | -0.012 |  |
| 2026-06-06 06:00:53 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-06 06:00:51 | Magura (Kalu Ganga) | 2.35 | 🟢 Normal | -0.013 |  |
| 2026-06-06 06:00:16 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 06:04:42 | Dunamale (Aththanagalu Oya) | 3.33 | 🟡 Alert | 0.000 |  |
| 2026-06-06 06:04:34 | Hanwella (Kelani Ganga) | 3.70 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-06 06:02:25 | Ellagawa (Kalu Ganga) | 7.24 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-06 06:03:12 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-06 06:03:53 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-06 06:00:53 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-05 18:01:21 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 06:01:56 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-06-06 06:02:29 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 06:01:05 | Nawalapitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-06 06:13:17 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-06 06:05:25 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-06 06:02:33 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 06:01:23 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-06 06:10:32 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-06 06:02:50 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-06 06:01:10 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-06 06:05:33 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-06 06:32:51 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | -0.001 |  |
| 2026-06-06 06:22:42 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.009 |  |
| 2026-06-06 06:05:28 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.009 |  |
| 2026-06-06 06:03:32 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-06-06 06:02:07 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-06-06 06:05:53 | Baddegama (Gin Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-06-06 06:02:29 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.010 |  |
| 2026-06-06 06:00:16 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.011 |  |
| 2026-06-06 06:00:58 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | -0.012 |  |
| 2026-06-06 06:00:51 | Magura (Kalu Ganga) | 2.35 | 🟢 Normal | -0.013 |  |
| 2026-06-06 05:16:55 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.016 |  |
| 2026-06-06 06:02:51 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.030 |  |
| 2026-06-06 06:03:19 | Deraniyagala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.030 |  |
| 2026-06-06 06:01:21 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | -0.046 |  |
| 2026-06-06 06:07:31 | Rathnapura (Kalu Ganga) | 3.30 | 🟢 Normal | -0.059 |  |
| 2026-06-06 06:03:15 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.061 |  |
| 2026-06-06 06:22:41 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | -0.068 |  |
| 2026-06-06 06:07:56 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.074 |  |
| 2026-06-06 06:05:37 | Glencourse (Kelani Ganga) | 11.80 | 🟢 Normal | -0.104 |  |
| 2026-06-06 06:02:02 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.115 |  |
| 2026-06-06 06:07:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.11 | 🟢 Normal | -0.161 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)