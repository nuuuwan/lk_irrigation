# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--13_10:06:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **16,657 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 10:06:16 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.066 |  |
| 2025-12-13 10:05:59 | Thanthirimale (Malwathu Oya) | 4.21 | 🟢 Normal | -0.009 |  |
| 2025-12-13 10:05:58 | Padiyathalawa (Maduru Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-13 10:05:51 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-13 10:05:08 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | -0.009 |  |
| 2025-12-13 10:04:46 | Putupaula (Kalu Ganga) | 1.16 | 🟢 Normal | -0.029 |  |
| 2025-12-13 10:04:45 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | -0.147 |  |
| 2025-12-13 10:04:21 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | -0.067 |  |
| 2025-12-13 10:03:58 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-13 10:03:46 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-13 10:03:43 | Glencourse (Kelani Ganga) | 9.49 | 🟢 Normal | -0.061 |  |
| 2025-12-13 10:03:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.57 | 🟢 Normal | -0.020 |  |
| 2025-12-13 10:03:20 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-13 10:03:09 | Weraganthota (Mahaweli Ganga) | -0.63 | 🟢 Normal | -0.220 |  |
| 2025-12-13 10:03:05 | Hanwella (Kelani Ganga) | 1.74 | 🟢 Normal | -0.020 |  |
| 2025-12-13 10:03:05 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-13 10:02:57 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.031 |  |
| 2025-12-13 10:02:54 | Galgamuwa (Mee Oya) | 1.70 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-13 10:02:53 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | -0.022 |  |
| 2025-12-13 10:02:41 | Urawa (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-13 10:02:31 | Moragaswewa (Deduru Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2025-12-13 10:02:13 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.041 |  |
| 2025-12-13 10:02:11 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-13 10:02:07 | Ellagawa (Kalu Ganga) | 5.78 | 🟢 Normal | -0.050 |  |
| 2025-12-13 10:01:55 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.379 |  |
| 2025-12-13 10:01:52 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-13 10:01:51 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 10:01:40 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-13 10:00:49 | Horowpothana (Yan Oya) | 5.92 | 🟢 Normal | -0.072 |  |
| 2025-12-13 10:00:49 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:16:51 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-13 09:14:24 | Manampitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.017 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 09:05:33 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2025-12-13 10:02:54 | Galgamuwa (Mee Oya) | 1.70 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-13 10:01:51 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 09:06:05 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-13 10:03:46 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-13 10:01:40 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:01:16 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-13 10:00:49 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-13 10:03:05 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:06:17 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-13 10:02:11 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:07:36 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | 0.000 |  |
| 2025-12-13 10:05:51 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-13 10:02:41 | Urawa (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:07:21 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-13 10:03:20 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-13 10:03:58 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-13 10:05:08 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | -0.009 |  |
| 2025-12-13 10:05:59 | Thanthirimale (Malwathu Oya) | 4.21 | 🟢 Normal | -0.009 |  |
| 2025-12-13 10:05:58 | Padiyathalawa (Maduru Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-13 10:02:31 | Moragaswewa (Deduru Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2025-12-13 10:01:52 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-13 09:14:24 | Manampitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.017 |  |
| 2025-12-13 10:03:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.57 | 🟢 Normal | -0.020 |  |
| 2025-12-13 10:03:05 | Hanwella (Kelani Ganga) | 1.74 | 🟢 Normal | -0.020 |  |
| 2025-12-13 09:02:30 | Magura (Kalu Ganga) | 2.68 | 🟢 Normal | -0.022 |  |
| 2025-12-13 10:02:53 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | -0.022 |  |
| 2025-12-13 10:04:46 | Putupaula (Kalu Ganga) | 1.16 | 🟢 Normal | -0.029 |  |
| 2025-12-13 10:02:57 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.031 |  |
| 2025-12-13 10:02:13 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.041 |  |
| 2025-12-13 10:02:07 | Ellagawa (Kalu Ganga) | 5.78 | 🟢 Normal | -0.050 |  |
| 2025-12-13 09:06:06 | Rathnapura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.060 |  |
| 2025-12-13 10:03:43 | Glencourse (Kelani Ganga) | 9.49 | 🟢 Normal | -0.061 |  |
| 2025-12-13 10:06:16 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.066 |  |
| 2025-12-13 10:04:21 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | -0.067 |  |
| 2025-12-13 10:00:49 | Horowpothana (Yan Oya) | 5.92 | 🟢 Normal | -0.072 |  |
| 2025-12-13 10:04:45 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | -0.147 |  |
| 2025-12-13 10:03:09 | Weraganthota (Mahaweli Ganga) | -0.63 | 🟢 Normal | -0.220 |  |
| 2025-12-13 10:01:55 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.379 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)