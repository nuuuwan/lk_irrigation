# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--12_04:34:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **285,526 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 04:34:42 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.049 |  |
| 2026-10-12 04:30:04 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-12 04:28:52 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-12 04:23:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.76 | 🟢 Normal | 0.841 | 🔺 Rising |
| 2026-10-12 04:16:49 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-10-12 04:13:37 | Holombuwa (Kelani Ganga) | 1.22 | 🟢 Normal | -0.062 |  |
| 2026-10-12 04:11:15 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.028 |  |
| 2026-10-12 04:10:07 | Panadugama (Nilwala Ganga) | 4.98 | 🟢 Normal | 0.000 |  |
| 2026-10-12 04:09:26 | Thawalama (Gin Ganga) | 3.31 | 🟢 Normal | -0.179 |  |
| 2026-10-12 04:07:06 | Dunamale (Aththanagalu Oya) | 2.86 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-12 04:06:59 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.029 |  |
| 2026-10-12 04:05:27 | Moragaswewa (Deduru Oya) | 1.37 | 🟢 Normal | -0.114 |  |
| 2026-10-12 04:05:03 | Hanwella (Kelani Ganga) | 3.90 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-12 04:04:57 | Urawa (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-10-12 04:03:54 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.028 |  |
| 2026-10-12 04:03:31 | Giriulla (Maha Oya) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-10-12 04:02:51 | Baddegama (Gin Ganga) | 2.55 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-12 04:02:42 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-12 04:02:38 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-12 04:02:35 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | -0.011 |  |
| 2026-10-12 04:02:27 | Ellagawa (Kalu Ganga) | 7.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-12 04:02:10 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | -0.020 |  |
| 2026-10-12 04:02:09 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 04:02:07 | Badalgama (Maha Oya) | 3.65 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-12 04:01:54 | Kithulgala (Kelani Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-10-12 04:01:54 | Glencourse (Kelani Ganga) | 11.88 | 🟢 Normal | -0.124 |  |
| 2026-10-12 04:01:46 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-12 04:01:43 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-12 04:01:34 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-10-12 04:01:25 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.021 |  |
| 2026-10-12 04:01:25 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.019 |  |
| 2026-10-12 04:01:06 | Rathnapura (Kalu Ganga) | 3.72 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-12 03:58:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.41 | 🟢 Normal | 0.841 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 04:23:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.76 | 🟢 Normal | 0.841 | 🔺 Rising |
| 2026-10-12 04:02:51 | Baddegama (Gin Ganga) | 2.55 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-12 04:02:07 | Badalgama (Maha Oya) | 3.65 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-12 04:01:06 | Rathnapura (Kalu Ganga) | 3.72 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-12 04:05:03 | Hanwella (Kelani Ganga) | 3.90 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-12 04:07:06 | Dunamale (Aththanagalu Oya) | 2.86 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-12 04:02:42 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-12 04:02:27 | Ellagawa (Kalu Ganga) | 7.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-12 03:06:16 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-12 04:16:49 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-10-11 18:00:16 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 04:02:09 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 04:01:54 | Kithulgala (Kelani Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-10-12 04:28:52 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-12 02:04:14 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 04:03:31 | Giriulla (Maha Oya) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-10-12 04:02:38 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 18:06:55 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-12 03:06:39 | Pitabeddara (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-10-12 04:10:07 | Panadugama (Nilwala Ganga) | 4.98 | 🟢 Normal | 0.000 |  |
| 2026-10-12 03:08:06 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-12 04:30:04 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-12 04:01:46 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-11 18:02:15 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.010 |  |
| 2026-10-12 04:02:35 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | -0.011 |  |
| 2026-10-12 04:01:25 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.019 |  |
| 2026-10-12 04:01:34 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-10-12 04:02:10 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | -0.020 |  |
| 2026-10-12 04:01:25 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.021 |  |
| 2026-10-12 04:04:57 | Urawa (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-10-12 04:11:15 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.028 |  |
| 2026-10-12 04:03:54 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.028 |  |
| 2026-10-12 04:06:59 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.029 |  |
| 2026-10-12 04:34:42 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.049 |  |
| 2026-10-12 04:13:37 | Holombuwa (Kelani Ganga) | 1.22 | 🟢 Normal | -0.062 |  |
| 2026-10-12 04:05:27 | Moragaswewa (Deduru Oya) | 1.37 | 🟢 Normal | -0.114 |  |
| 2026-10-12 04:01:54 | Glencourse (Kelani Ganga) | 11.88 | 🟢 Normal | -0.124 |  |
| 2026-10-12 03:04:17 | Magura (Kalu Ganga) | 3.32 | 🟢 Normal | -0.161 |  |
| 2026-10-12 04:09:26 | Thawalama (Gin Ganga) | 3.31 | 🟢 Normal | -0.179 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)