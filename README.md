# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_08:16:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **153,230 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 08:16:54 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | -0.008 |  |
| 2026-05-16 08:12:14 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.044 |  |
| 2026-05-16 08:11:43 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-16 08:10:53 | Badalgama (Maha Oya) | 3.65 | 🟢 Normal | -0.029 |  |
| 2026-05-16 08:09:23 | Baddegama (Gin Ganga) | 2.97 | 🟢 Normal | -0.028 |  |
| 2026-05-16 08:07:44 | Rathnapura (Kalu Ganga) | 3.54 | 🟢 Normal | -0.021 |  |
| 2026-05-16 08:07:22 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | -0.019 |  |
| 2026-05-16 08:07:08 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-16 08:07:04 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-16 08:06:09 | Putupaula (Kalu Ganga) | 2.91 | 🟢 Normal | 0.000 |  |
| 2026-05-16 08:05:30 | Panadugama (Nilwala Ganga) | 3.60 | 🟢 Normal | -0.089 |  |
| 2026-05-16 08:05:20 | Galgamuwa (Mee Oya) | 3.65 | 🟢 Normal | -0.028 |  |
| 2026-05-16 08:04:27 | Katharagama (Menik Ganga) | 0.23 | 🟢 Normal | -0.043 |  |
| 2026-05-16 08:04:17 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-05-16 08:04:15 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-16 08:04:06 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-05-16 08:03:32 | Dunamale (Aththanagalu Oya) | 4.38 | 🟡 Alert | -0.046 |  |
| 2026-05-16 08:03:30 | Giriulla (Maha Oya) | 2.50 | 🟢 Normal | -0.059 |  |
| 2026-05-16 08:03:27 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.059 |  |
| 2026-05-16 08:03:27 | Magura (Kalu Ganga) | 3.70 | 🟢 Normal | -0.044 |  |
| 2026-05-16 08:03:25 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.019 |  |
| 2026-05-16 08:03:19 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.061 |  |
| 2026-05-16 08:03:14 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-16 08:02:59 | Glencourse (Kelani Ganga) | 11.19 | 🟢 Normal | 0.000 |  |
| 2026-05-16 08:02:30 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.155 |  |
| 2026-05-16 08:02:28 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-16 08:02:25 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-05-16 08:02:19 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.013 |  |
| 2026-05-16 08:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.05 | 🟠 Minor Flood | -0.010 |  |
| 2026-05-16 08:01:57 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-16 08:01:45 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.117 |  |
| 2026-05-16 08:01:26 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-05-16 08:01:21 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-05-16 08:01:11 | Ellagawa (Kalu Ganga) | 8.50 | 🟢 Normal | -0.051 |  |
| 2026-05-16 08:01:10 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-05-16 08:01:06 | Thanthirimale (Malwathu Oya) | 4.08 | 🟢 Normal | -0.021 |  |
| 2026-05-16 08:00:26 | Moragaswewa (Deduru Oya) | 3.04 | 🟢 Normal | -0.033 |  |
| 2026-05-16 07:42:07 | Moragaswewa (Deduru Oya) | 3.05 | 🟢 Normal | -0.033 |  |
| 2026-05-16 07:37:53 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.024 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 08:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.05 | 🟠 Minor Flood | -0.010 |  |
| 2026-05-16 08:03:32 | Dunamale (Aththanagalu Oya) | 4.38 | 🟡 Alert | -0.046 |  |
| 2026-05-16 08:03:14 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-16 07:01:39 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 08:11:43 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-16 08:07:08 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-16 08:04:15 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-16 08:02:59 | Glencourse (Kelani Ganga) | 11.19 | 🟢 Normal | 0.000 |  |
| 2026-05-16 08:01:21 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-05-16 08:04:17 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-05-16 08:06:09 | Putupaula (Kalu Ganga) | 2.91 | 🟢 Normal | 0.000 |  |
| 2026-05-16 08:07:04 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-16 08:04:06 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-05-16 08:02:28 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-16 08:16:54 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | -0.008 |  |
| 2026-05-16 08:01:57 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-16 08:02:25 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-05-16 08:01:26 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-05-16 08:01:10 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-05-16 08:02:19 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.013 |  |
| 2026-05-16 08:07:22 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | -0.019 |  |
| 2026-05-16 08:03:25 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.019 |  |
| 2026-05-16 08:07:44 | Rathnapura (Kalu Ganga) | 3.54 | 🟢 Normal | -0.021 |  |
| 2026-05-16 08:01:06 | Thanthirimale (Malwathu Oya) | 4.08 | 🟢 Normal | -0.021 |  |
| 2026-05-16 08:09:23 | Baddegama (Gin Ganga) | 2.97 | 🟢 Normal | -0.028 |  |
| 2026-05-16 08:05:20 | Galgamuwa (Mee Oya) | 3.65 | 🟢 Normal | -0.028 |  |
| 2026-05-16 08:10:53 | Badalgama (Maha Oya) | 3.65 | 🟢 Normal | -0.029 |  |
| 2026-05-16 08:00:26 | Moragaswewa (Deduru Oya) | 3.04 | 🟢 Normal | -0.033 |  |
| 2026-05-16 08:04:27 | Katharagama (Menik Ganga) | 0.23 | 🟢 Normal | -0.043 |  |
| 2026-05-16 08:03:27 | Magura (Kalu Ganga) | 3.70 | 🟢 Normal | -0.044 |  |
| 2026-05-16 08:12:14 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.044 |  |
| 2026-05-16 08:01:11 | Ellagawa (Kalu Ganga) | 8.50 | 🟢 Normal | -0.051 |  |
| 2026-05-16 08:03:30 | Giriulla (Maha Oya) | 2.50 | 🟢 Normal | -0.059 |  |
| 2026-05-16 07:01:08 | Horowpothana (Yan Oya) | 2.64 | 🟢 Normal | -0.059 |  |
| 2026-05-16 08:03:27 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.059 |  |
| 2026-05-16 08:03:19 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.061 |  |
| 2026-05-16 08:05:30 | Panadugama (Nilwala Ganga) | 3.60 | 🟢 Normal | -0.089 |  |
| 2026-05-16 08:01:45 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.117 |  |
| 2026-05-16 08:02:30 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.155 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)