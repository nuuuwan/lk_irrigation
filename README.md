# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_07:15:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **153,190 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 07:15:53 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-05-16 07:15:43 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.008 |  |
| 2026-05-16 07:12:00 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-16 07:11:40 | Dunamale (Aththanagalu Oya) | 4.42 | 🟠 Minor Flood | -0.026 |  |
| 2026-05-16 07:11:07 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.009 |  |
| 2026-05-16 07:10:30 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-16 07:10:23 | Rathnapura (Kalu Ganga) | 3.56 | 🟢 Normal | -0.065 |  |
| 2026-05-16 07:09:31 | Badalgama (Maha Oya) | 3.68 | 🟢 Normal | -0.045 |  |
| 2026-05-16 07:09:08 | Katharagama (Menik Ganga) | 0.27 | 🟢 Normal | -0.019 |  |
| 2026-05-16 07:08:22 | Magura (Kalu Ganga) | 3.74 | 🟢 Normal | -0.075 |  |
| 2026-05-16 07:07:34 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-05-16 07:06:02 | Glencourse (Kelani Ganga) | 11.19 | 🟢 Normal | 0.000 |  |
| 2026-05-16 07:05:57 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | -0.076 |  |
| 2026-05-16 07:04:55 | Baddegama (Gin Ganga) | 3.00 | 🟢 Normal | -0.021 |  |
| 2026-05-16 07:04:54 | Hanwella (Kelani Ganga) | 4.02 | 🟢 Normal | -0.078 |  |
| 2026-05-16 07:04:54 | Glencourse (Kelani Ganga) | 11.19 | 🟢 Normal | 0.000 |  |
| 2026-05-16 07:04:43 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-16 07:04:37 | Panadugama (Nilwala Ganga) | 3.69 | 🟢 Normal | -0.111 |  |
| 2026-05-16 07:04:36 | Thanthirimale (Malwathu Oya) | 4.10 | 🟢 Normal | -0.006 |  |
| 2026-05-16 07:04:28 | Putupaula (Kalu Ganga) | 2.91 | 🟢 Normal | -0.041 |  |
| 2026-05-16 07:04:23 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-05-16 07:02:39 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.021 |  |
| 2026-05-16 07:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.06 | 🟠 Minor Flood | -0.041 |  |
| 2026-05-16 07:02:11 | Giriulla (Maha Oya) | 2.56 | 🟢 Normal | -0.071 |  |
| 2026-05-16 07:02:09 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | -0.033 |  |
| 2026-05-16 07:02:08 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-16 07:01:51 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-05-16 07:01:47 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.020 |  |
| 2026-05-16 07:01:40 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.104 |  |
| 2026-05-16 07:01:39 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 07:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.049 |  |
| 2026-05-16 07:01:08 | Horowpothana (Yan Oya) | 2.64 | 🟢 Normal | -0.059 |  |
| 2026-05-16 07:01:08 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-05-16 07:00:53 | Galgamuwa (Mee Oya) | 3.68 | 🟢 Normal | -0.041 |  |
| 2026-05-16 07:00:45 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.020 |  |
| 2026-05-16 07:00:32 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-05-16 07:00:13 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.020 |  |
| 2026-05-16 06:59:38 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | -0.012 |  |
| 2026-05-16 06:32:19 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | -0.111 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 07:11:40 | Dunamale (Aththanagalu Oya) | 4.42 | 🟠 Minor Flood | -0.026 |  |
| 2026-05-16 07:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.06 | 🟠 Minor Flood | -0.041 |  |
| 2026-05-16 07:04:43 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-16 07:01:39 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 06:28:19 | Moragaswewa (Deduru Oya) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-05-16 07:12:00 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-16 07:10:30 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-16 07:06:02 | Glencourse (Kelani Ganga) | 11.19 | 🟢 Normal | 0.000 |  |
| 2026-05-16 07:15:53 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-05-16 07:00:32 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-05-16 07:02:08 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-16 07:04:36 | Thanthirimale (Malwathu Oya) | 4.10 | 🟢 Normal | -0.006 |  |
| 2026-05-16 07:15:43 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.008 |  |
| 2026-05-16 07:11:07 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.009 |  |
| 2026-05-16 06:00:21 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.011 |  |
| 2026-05-16 06:59:38 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | -0.012 |  |
| 2026-05-16 07:09:08 | Katharagama (Menik Ganga) | 0.27 | 🟢 Normal | -0.019 |  |
| 2026-05-16 07:01:47 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.020 |  |
| 2026-05-16 07:00:13 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.020 |  |
| 2026-05-16 07:01:08 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-05-16 07:01:51 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-05-16 07:04:23 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-05-16 07:00:45 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.020 |  |
| 2026-05-16 07:02:39 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.021 |  |
| 2026-05-16 07:04:55 | Baddegama (Gin Ganga) | 3.00 | 🟢 Normal | -0.021 |  |
| 2026-05-16 07:02:09 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | -0.033 |  |
| 2026-05-16 07:00:53 | Galgamuwa (Mee Oya) | 3.68 | 🟢 Normal | -0.041 |  |
| 2026-05-16 07:04:28 | Putupaula (Kalu Ganga) | 2.91 | 🟢 Normal | -0.041 |  |
| 2026-05-16 07:09:31 | Badalgama (Maha Oya) | 3.68 | 🟢 Normal | -0.045 |  |
| 2026-05-16 07:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.049 |  |
| 2026-05-16 07:01:08 | Horowpothana (Yan Oya) | 2.64 | 🟢 Normal | -0.059 |  |
| 2026-05-16 07:10:23 | Rathnapura (Kalu Ganga) | 3.56 | 🟢 Normal | -0.065 |  |
| 2026-05-16 07:02:11 | Giriulla (Maha Oya) | 2.56 | 🟢 Normal | -0.071 |  |
| 2026-05-16 07:08:22 | Magura (Kalu Ganga) | 3.74 | 🟢 Normal | -0.075 |  |
| 2026-05-16 07:05:57 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | -0.076 |  |
| 2026-05-16 07:04:54 | Hanwella (Kelani Ganga) | 4.02 | 🟢 Normal | -0.078 |  |
| 2026-05-16 07:01:40 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.104 |  |
| 2026-05-16 07:04:37 | Panadugama (Nilwala Ganga) | 3.69 | 🟢 Normal | -0.111 |  |
| 2026-05-16 06:07:55 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)