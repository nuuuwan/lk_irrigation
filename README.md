# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--06_07:19:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **280,252 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 07:19:35 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.023 |  |
| 2026-10-06 07:15:48 | Badalgama (Maha Oya) | 3.15 | 🟢 Normal | -0.008 |  |
| 2026-10-06 07:10:20 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.057 |  |
| 2026-10-06 07:08:58 | Magura (Kalu Ganga) | 2.92 | 🟢 Normal | -0.065 |  |
| 2026-10-06 07:08:38 | Thawalama (Gin Ganga) | 2.33 | 🟢 Normal | -0.156 |  |
| 2026-10-06 07:08:12 | Peradeniya (Mahaweli Ganga) | 3.04 | 🟢 Normal | 0.000 |  |
| 2026-10-06 07:07:31 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-06 07:07:09 | Panadugama (Nilwala Ganga) | 4.01 | 🟢 Normal | -0.049 |  |
| 2026-10-06 07:06:06 | Hanwella (Kelani Ganga) | 4.21 | 🟢 Normal | -0.102 |  |
| 2026-10-06 07:05:52 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-10-06 07:05:47 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.018 |  |
| 2026-10-06 07:05:38 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-10-06 07:05:34 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-06 07:05:30 | Rathnapura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.028 |  |
| 2026-10-06 07:04:36 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.029 |  |
| 2026-10-06 07:04:36 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-06 07:04:24 | Giriulla (Maha Oya) | 1.89 | 🟢 Normal | -0.058 |  |
| 2026-10-06 07:04:05 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-06 07:04:02 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-06 07:03:41 | Dunamale (Aththanagalu Oya) | 2.59 | 🟢 Normal | -0.020 |  |
| 2026-10-06 07:03:24 | Glencourse (Kelani Ganga) | 11.98 | 🟢 Normal | -0.129 |  |
| 2026-10-06 07:03:21 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-06 07:03:19 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-06 07:03:03 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-06 07:03:00 | Ellagawa (Kalu Ganga) | 6.14 | 🟢 Normal | 0.000 |  |
| 2026-10-06 07:02:52 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-10-06 07:02:52 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.032 |  |
| 2026-10-06 07:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.75 | 🟢 Normal | 0.337 | 🔺 Rising |
| 2026-10-06 07:02:26 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-06 07:02:11 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-10-06 07:02:09 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-06 07:02:07 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-10-06 07:01:41 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-06 07:01:41 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | 0.003 |  |
| 2026-10-06 07:01:39 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 07:01:36 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.041 |  |
| 2026-10-06 07:01:32 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.030 |  |
| 2026-10-06 07:00:51 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-06 07:00:51 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 07:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.75 | 🟢 Normal | 0.337 | 🔺 Rising |
| 2026-10-06 07:03:21 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-06 07:05:34 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-06 07:07:31 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-06 07:04:36 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-06 07:01:41 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | 0.003 |  |
| 2026-10-06 07:04:02 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-06 07:01:39 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 07:03:03 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-06 07:01:41 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-06 07:00:51 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-06 07:03:00 | Ellagawa (Kalu Ganga) | 6.14 | 🟢 Normal | 0.000 |  |
| 2026-10-06 07:04:05 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-06 07:02:26 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-06 07:03:19 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-06 07:02:09 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-06 07:08:12 | Peradeniya (Mahaweli Ganga) | 3.04 | 🟢 Normal | 0.000 |  |
| 2026-10-06 07:00:51 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-06 07:15:48 | Badalgama (Maha Oya) | 3.15 | 🟢 Normal | -0.008 |  |
| 2026-10-06 07:05:52 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-10-06 07:02:11 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-10-06 07:02:52 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-10-06 07:05:47 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.018 |  |
| 2026-10-06 07:03:41 | Dunamale (Aththanagalu Oya) | 2.59 | 🟢 Normal | -0.020 |  |
| 2026-10-06 07:05:38 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-10-06 07:02:07 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-10-06 07:19:35 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.023 |  |
| 2026-10-06 07:05:30 | Rathnapura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.028 |  |
| 2026-10-06 07:04:36 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.029 |  |
| 2026-10-06 07:01:32 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.030 |  |
| 2026-10-06 07:02:52 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.032 |  |
| 2026-10-06 07:01:36 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.041 |  |
| 2026-10-06 07:07:09 | Panadugama (Nilwala Ganga) | 4.01 | 🟢 Normal | -0.049 |  |
| 2026-10-06 07:10:20 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.057 |  |
| 2026-10-06 07:04:24 | Giriulla (Maha Oya) | 1.89 | 🟢 Normal | -0.058 |  |
| 2026-10-06 07:08:58 | Magura (Kalu Ganga) | 2.92 | 🟢 Normal | -0.065 |  |
| 2026-10-06 07:06:06 | Hanwella (Kelani Ganga) | 4.21 | 🟢 Normal | -0.102 |  |
| 2026-10-06 07:03:24 | Glencourse (Kelani Ganga) | 11.98 | 🟢 Normal | -0.129 |  |
| 2026-10-06 07:08:38 | Thawalama (Gin Ganga) | 2.33 | 🟢 Normal | -0.156 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)