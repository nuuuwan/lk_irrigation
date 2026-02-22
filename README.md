# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--22_07:01:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **79,730 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 07:01:00 | Thanamalwila (Kirindi Oya) | 1.93 | 🟢 Normal | -1.312 |  |
| 2026-02-22 07:00:37 | Kuda Oya (Kirindi Oya) | 2.42 | 🟢 Normal | -0.012 |  |
| 2026-02-22 07:00:36 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-02-22 07:00:18 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.050 |  |
| 2026-02-22 07:00:09 | Padiyathalawa (Maduru Oya) | 1.53 | 🟢 Normal | -0.025 |  |
| 2026-02-22 07:00:06 | Nakkala (Kumbukkan Oya) | 1.56 | 🟢 Normal | -0.062 |  |
| 2026-02-22 06:30:35 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 06:18:22 | Thalgahagoda (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-02-22 06:12:32 | Padiyathalawa (Maduru Oya) | 1.55 | 🟢 Normal | -0.025 |  |
| 2026-02-22 06:12:30 | Padiyathalawa (Maduru Oya) | 1.57 | 🟢 Normal | -0.025 |  |
| 2026-02-22 06:12:29 | Padiyathalawa (Maduru Oya) | 1.60 | 🟢 Normal | -0.025 |  |
| 2026-02-22 06:12:12 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | 0.244 | 🔺 Rising |
| 2026-02-22 06:11:47 | Kuda Oya (Kirindi Oya) | 2.43 | 🟢 Normal | -0.012 |  |
| 2026-02-22 06:11:23 | Panadugama (Nilwala Ganga) | 4.33 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-22 06:11:21 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-22 06:10:58 | Glencourse (Kelani Ganga) | 11.24 | 🟢 Normal | -0.182 |  |
| 2026-02-22 06:10:36 | Thawalama (Gin Ganga) | 3.22 | 🟢 Normal | -0.115 |  |
| 2026-02-22 06:09:00 | Rathnapura (Kalu Ganga) | 4.65 | 🟢 Normal | -0.094 |  |
| 2026-02-22 06:08:59 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-02-22 06:08:19 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.564 |  |
| 2026-02-22 06:08:14 | Ellagawa (Kalu Ganga) | 7.47 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-02-22 06:07:56 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-22 06:06:33 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 06:05:50 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.096 |  |
| 2026-02-22 06:05:31 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.050 |  |
| 2026-02-22 06:05:29 | Pitabeddara (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.268 |  |
| 2026-02-22 06:05:20 | Manampitiya (Mahaweli Ganga) | 4.40 | 🟠 Minor Flood | 0.093 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 06:05:20 | Manampitiya (Mahaweli Ganga) | 4.40 | 🟠 Minor Flood | 0.093 | 🔺 Rising |
| 2026-02-22 06:03:25 | Giriulla (Maha Oya) | 2.63 | 🟢 Normal | 1.890 | 🔺 Rising |
| 2026-02-22 06:04:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.26 | 🟢 Normal | 1.818 | 🔺 Rising |
| 2026-02-22 06:02:08 | Hanwella (Kelani Ganga) | 2.95 | 🟢 Normal | 0.446 | 🔺 Rising |
| 2026-02-22 06:01:55 | Magura (Kalu Ganga) | 3.46 | 🟢 Normal | 0.438 | 🔺 Rising |
| 2026-02-22 06:01:47 | Putupaula (Kalu Ganga) | 1.26 | 🟢 Normal | 0.271 | 🔺 Rising |
| 2026-02-22 06:12:12 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | 0.244 | 🔺 Rising |
| 2026-02-22 07:00:36 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-02-22 06:08:14 | Ellagawa (Kalu Ganga) | 7.47 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-02-22 06:00:33 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-22 06:00:14 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-22 06:11:23 | Panadugama (Nilwala Ganga) | 4.33 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-22 06:04:28 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-21 18:05:22 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-22 06:02:27 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | 0.002 |  |
| 2026-02-22 06:08:59 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-02-22 06:11:21 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-22 06:01:36 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-22 06:30:35 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 06:03:01 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-02-22 06:06:33 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 06:07:56 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-22 07:00:37 | Kuda Oya (Kirindi Oya) | 2.42 | 🟢 Normal | -0.012 |  |
| 2026-02-22 06:04:34 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | -0.021 |  |
| 2026-02-22 07:00:09 | Padiyathalawa (Maduru Oya) | 1.53 | 🟢 Normal | -0.025 |  |
| 2026-02-22 06:03:21 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.041 |  |
| 2026-02-22 06:05:31 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.050 |  |
| 2026-02-22 07:00:18 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.050 |  |
| 2026-02-22 06:04:27 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.061 |  |
| 2026-02-22 07:00:06 | Nakkala (Kumbukkan Oya) | 1.56 | 🟢 Normal | -0.062 |  |
| 2026-02-22 06:09:00 | Rathnapura (Kalu Ganga) | 4.65 | 🟢 Normal | -0.094 |  |
| 2026-02-22 06:05:50 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.096 |  |
| 2026-02-22 06:04:29 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.101 |  |
| 2026-02-22 06:10:36 | Thawalama (Gin Ganga) | 3.22 | 🟢 Normal | -0.115 |  |
| 2026-02-22 06:10:58 | Glencourse (Kelani Ganga) | 11.24 | 🟢 Normal | -0.182 |  |
| 2026-02-22 06:05:29 | Pitabeddara (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.268 |  |
| 2026-02-22 06:08:19 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.564 |  |
| 2026-02-22 06:04:49 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.735 |  |
| 2026-02-22 07:01:00 | Thanamalwila (Kirindi Oya) | 1.93 | 🟢 Normal | -1.312 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)