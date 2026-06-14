# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--14_22:15:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **179,506 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 22:15:20 | Rathnapura (Kalu Ganga) | 2.68 | 🟢 Normal | -0.058 |  |
| 2026-06-14 22:11:28 | Putupaula (Kalu Ganga) | 2.57 | 🟢 Normal | -0.028 |  |
| 2026-06-14 22:11:15 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-06-14 22:09:46 | Baddegama (Gin Ganga) | 2.44 | 🟢 Normal | -0.043 |  |
| 2026-06-14 22:09:43 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.009 |  |
| 2026-06-14 22:08:12 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.037 |  |
| 2026-06-14 22:07:33 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.020 |  |
| 2026-06-14 22:06:53 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | -0.010 |  |
| 2026-06-14 22:06:13 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-06-14 22:05:55 | Panadugama (Nilwala Ganga) | 3.55 | 🟢 Normal | -0.013 |  |
| 2026-06-14 22:04:57 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-14 22:04:42 | Giriulla (Maha Oya) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-06-14 22:04:03 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | -0.031 |  |
| 2026-06-14 22:04:01 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-14 22:03:45 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.020 |  |
| 2026-06-14 22:03:45 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-14 22:03:43 | Peradeniya (Mahaweli Ganga) | 2.31 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-06-14 22:03:28 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-06-14 22:03:18 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-14 22:02:56 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-14 22:02:36 | Hanwella (Kelani Ganga) | 3.02 | 🟢 Normal | -0.060 |  |
| 2026-06-14 22:02:22 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-14 22:02:03 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.040 |  |
| 2026-06-14 22:01:53 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-14 22:01:41 | Ellagawa (Kalu Ganga) | 7.62 | 🟢 Normal | -0.124 |  |
| 2026-06-14 22:01:41 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-14 22:01:29 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-14 22:01:28 | Moragaswewa (Deduru Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-06-14 22:01:24 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-14 22:01:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.98 | 🟡 Alert | -0.030 |  |
| 2026-06-14 22:00:57 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-06-14 22:00:14 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-14 22:00:08 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 22:01:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.98 | 🟡 Alert | -0.030 |  |
| 2026-06-14 22:03:43 | Peradeniya (Mahaweli Ganga) | 2.31 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-06-14 22:04:01 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-14 22:04:57 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-14 22:00:08 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-14 22:01:29 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-14 22:01:53 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-14 21:03:10 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-14 22:03:45 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-14 22:00:14 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-14 22:01:24 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-14 22:01:41 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-14 22:02:56 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-14 22:03:18 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-14 22:02:22 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-14 22:09:43 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.009 |  |
| 2026-06-14 22:11:15 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-06-14 18:04:23 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.009 |  |
| 2026-06-14 21:03:36 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-06-14 18:01:41 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-06-14 22:06:53 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | -0.010 |  |
| 2026-06-14 22:01:28 | Moragaswewa (Deduru Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-06-14 22:06:13 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-06-14 22:00:57 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-06-14 22:05:55 | Panadugama (Nilwala Ganga) | 3.55 | 🟢 Normal | -0.013 |  |
| 2026-06-14 22:03:45 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.020 |  |
| 2026-06-14 22:04:42 | Giriulla (Maha Oya) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-06-14 22:07:33 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.020 |  |
| 2026-06-14 22:03:28 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-06-14 18:03:42 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-06-14 22:11:28 | Putupaula (Kalu Ganga) | 2.57 | 🟢 Normal | -0.028 |  |
| 2026-06-14 21:04:02 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | -0.029 |  |
| 2026-06-14 22:04:03 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | -0.031 |  |
| 2026-06-14 22:08:12 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.037 |  |
| 2026-06-14 22:02:03 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.040 |  |
| 2026-06-14 22:09:46 | Baddegama (Gin Ganga) | 2.44 | 🟢 Normal | -0.043 |  |
| 2026-06-14 22:15:20 | Rathnapura (Kalu Ganga) | 2.68 | 🟢 Normal | -0.058 |  |
| 2026-06-14 22:02:36 | Hanwella (Kelani Ganga) | 3.02 | 🟢 Normal | -0.060 |  |
| 2026-06-14 22:01:41 | Ellagawa (Kalu Ganga) | 7.62 | 🟢 Normal | -0.124 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)