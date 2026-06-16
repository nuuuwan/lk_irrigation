# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--16_15:03:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **180,997 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-16 15:03:23 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-16 15:03:22 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.021 |  |
| 2026-06-16 15:03:13 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-16 15:03:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.65 | 🟢 Normal | -0.011 |  |
| 2026-06-16 15:02:58 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-06-16 15:02:50 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-06-16 15:02:44 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-16 15:02:37 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-16 15:02:33 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.050 |  |
| 2026-06-16 15:02:12 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-16 15:02:04 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-06-16 15:02:00 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.010 |  |
| 2026-06-16 15:01:30 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-16 15:01:23 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-16 15:01:20 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-16 15:01:10 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.021 |  |
| 2026-06-16 15:00:45 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 15:00:43 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.022 |  |
| 2026-06-16 15:00:34 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-16 15:00:21 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-16 15:00:18 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-06-16 14:56:43 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-16 14:34:21 | Magura (Kalu Ganga) | 2.45 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-06-16 14:13:07 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-16 14:08:06 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-06-16 14:05:37 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-06-16 15:02:44 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-16 15:00:45 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 14:34:21 | Magura (Kalu Ganga) | 2.45 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-06-16 15:01:20 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-16 15:01:30 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-16 14:02:19 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-16 15:02:58 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-06-16 14:56:43 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-16 14:02:25 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-16 14:00:58 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-16 15:03:13 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-16 14:06:28 | Ellagawa (Kalu Ganga) | 5.75 | 🟢 Normal | 0.000 |  |
| 2026-06-16 14:03:50 | Baddegama (Gin Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-06-16 14:06:35 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | 0.000 |  |
| 2026-06-16 15:03:23 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-16 15:01:23 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-16 15:00:21 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-16 14:10:35 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-06-16 15:02:12 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-16 14:05:56 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-06-16 14:05:15 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-16 14:13:07 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-16 15:00:34 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-16 15:02:37 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-16 15:02:00 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.010 |  |
| 2026-06-16 15:02:04 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-06-16 15:02:50 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-06-16 15:00:18 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-06-16 14:09:48 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.011 |  |
| 2026-06-16 15:03:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.65 | 🟢 Normal | -0.011 |  |
| 2026-06-16 14:09:53 | Rathnapura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.020 |  |
| 2026-06-16 15:03:22 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.021 |  |
| 2026-06-16 15:01:10 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.021 |  |
| 2026-06-16 15:00:43 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.022 |  |
| 2026-06-16 14:02:16 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | -0.031 |  |
| 2026-06-16 15:02:33 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.050 |  |
| 2026-06-16 14:09:50 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)