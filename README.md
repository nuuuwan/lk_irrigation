# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_18:24:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **125,058 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 18:24:13 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 18:17:02 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-14 18:15:46 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-14 18:10:23 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.011 |  |
| 2026-04-14 18:09:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.11 | 🟢 Normal | -0.027 |  |
| 2026-04-14 18:08:59 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.059 |  |
| 2026-04-14 18:07:36 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | -0.051 |  |
| 2026-04-14 18:07:35 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.009 |  |
| 2026-04-14 18:07:18 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-14 18:07:11 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | -0.036 |  |
| 2026-04-14 18:06:57 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-14 18:06:46 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.048 |  |
| 2026-04-14 18:06:01 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-14 18:05:44 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-14 18:05:05 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | -0.030 |  |
| 2026-04-14 18:04:32 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | -0.010 |  |
| 2026-04-14 18:03:54 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-04-14 18:03:31 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-14 18:03:27 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-14 18:03:03 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-04-14 18:03:03 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-04-14 18:02:56 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | -0.020 |  |
| 2026-04-14 18:02:56 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-04-14 18:02:35 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-14 18:02:24 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.021 |  |
| 2026-04-14 18:02:21 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.104 |  |
| 2026-04-14 18:02:11 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-14 18:01:59 | Thanthirimale (Malwathu Oya) | 3.79 | 🟢 Normal | -0.059 |  |
| 2026-04-14 18:01:58 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-04-14 18:01:18 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-14 18:00:52 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.022 |  |
| 2026-04-14 18:00:32 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-14 18:00:27 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.094 |  |
| 2026-04-14 18:00:15 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-04-14 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.063 |  |
| 2026-04-14 18:00:09 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 17:54:09 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | -0.048 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 18:03:03 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-04-14 18:02:56 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-04-14 18:15:46 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-14 18:17:02 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-14 18:00:09 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 18:00:32 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:16:46 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 18:24:13 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 18:02:11 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-14 18:03:31 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-14 18:01:18 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-14 18:06:01 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-14 18:07:18 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-14 18:03:27 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-14 18:03:54 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-04-14 18:05:44 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-14 18:02:35 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-14 18:03:03 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-04-14 18:06:57 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-14 18:07:35 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.009 |  |
| 2026-04-14 18:04:32 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | -0.010 |  |
| 2026-04-14 17:00:31 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-04-14 18:00:15 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-04-14 18:10:23 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.011 |  |
| 2026-04-14 17:01:24 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-04-14 18:02:56 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | -0.020 |  |
| 2026-04-14 18:02:24 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.021 |  |
| 2026-04-14 18:01:58 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-04-14 18:00:52 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.022 |  |
| 2026-04-14 18:09:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.11 | 🟢 Normal | -0.027 |  |
| 2026-04-14 18:05:05 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | -0.030 |  |
| 2026-04-14 18:07:11 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | -0.036 |  |
| 2026-04-14 18:06:46 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.048 |  |
| 2026-04-14 18:07:36 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | -0.051 |  |
| 2026-04-14 18:01:59 | Thanthirimale (Malwathu Oya) | 3.79 | 🟢 Normal | -0.059 |  |
| 2026-04-14 18:08:59 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.059 |  |
| 2026-04-14 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.063 |  |
| 2026-04-14 18:00:27 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.094 |  |
| 2026-04-14 18:02:21 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.104 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)