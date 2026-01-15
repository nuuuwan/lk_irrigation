# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--15_08:05:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **46,058 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 08:05:53 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:05:41 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-01-15 08:05:29 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:05:25 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:04:31 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:04:30 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:04:19 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-01-15 08:04:03 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.066 |  |
| 2026-01-15 08:04:02 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:03:50 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-01-15 08:03:48 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.079 |  |
| 2026-01-15 08:03:46 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.030 |  |
| 2026-01-15 08:03:29 | Glencourse (Kelani Ganga) | 8.69 | 🟢 Normal | -0.061 |  |
| 2026-01-15 08:03:19 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.033 |  |
| 2026-01-15 08:03:18 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:03:17 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:02:52 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | -0.051 |  |
| 2026-01-15 08:02:41 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-15 08:02:36 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:02:23 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | -0.028 |  |
| 2026-01-15 08:02:17 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:02:12 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:02:05 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | -0.010 |  |
| 2026-01-15 08:01:55 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:01:52 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:01:43 | Thanthirimale (Malwathu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:01:30 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:01:29 | Manampitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.029 |  |
| 2026-01-15 08:01:23 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:01:08 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.025 |  |
| 2026-01-15 08:00:39 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:00:36 | Peradeniya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.012 |  |
| 2026-01-15 07:57:35 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:41:07 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.029 |  |
| 2026-01-15 07:19:58 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | -0.028 |  |
| 2026-01-15 07:15:12 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:12:24 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.025 |  |
| 2026-01-15 07:10:30 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 08:02:41 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-15 06:07:27 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 07:02:59 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 08:02:17 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:02:36 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:00:39 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:01:30 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:01:52 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:07:52 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:03:34 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:01:55 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:04:30 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:05:29 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:02:12 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:04:02 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:01:23 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:03:17 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:04:31 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:05:53 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:01:43 | Thanthirimale (Malwathu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:05:25 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:03:18 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-15 08:03:50 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-01-15 08:02:05 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | -0.010 |  |
| 2026-01-15 08:05:41 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-01-15 08:00:36 | Peradeniya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.012 |  |
| 2026-01-15 08:04:19 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-01-15 08:01:08 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.025 |  |
| 2026-01-15 08:02:23 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | -0.028 |  |
| 2026-01-15 08:01:29 | Manampitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.029 |  |
| 2026-01-15 08:03:46 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.030 |  |
| 2026-01-15 08:03:19 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.033 |  |
| 2026-01-15 08:02:52 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | -0.051 |  |
| 2026-01-15 08:03:29 | Glencourse (Kelani Ganga) | 8.69 | 🟢 Normal | -0.061 |  |
| 2026-01-15 08:04:03 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.066 |  |
| 2026-01-15 08:03:48 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.079 |  |
| 2026-01-15 07:08:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.03 | 🟢 Normal | -0.126 |  |
| 2026-01-15 07:02:55 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | -0.156 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)